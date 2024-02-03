import os

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from bot.lexicons.lexicon_ru import LEXICON_RU
from bot.users.users import USERS_UPSCALE_STATE

router = Router()


@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    user_id = message.from_user.id
    USERS_UPSCALE_STATE[user_id] = False
    await message.answer(LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    user_id = message.from_user.id
    USERS_UPSCALE_STATE[user_id] = False
    await message.answer(LEXICON_RU['/help'])


@router.message(Command(commands='upscale_image'))
async def process_upscale_image_command(message: Message):
    user_id = message.from_user.id
    USERS_UPSCALE_STATE[user_id] = True
    await message.answer(LEXICON_RU['/upscale_image'])


@router.message(F.content_type == 'photo')
async def process_photo_command(message: Message):
    user_id = message.from_user.id
    if user_id not in USERS_UPSCALE_STATE.keys():
        USERS_UPSCALE_STATE[user_id] = False
    if USERS_UPSCALE_STATE[user_id]:
        file_id = message.photo[-1].file_id
        await message.bot.download(file=file_id, destination=f'bot/downloads/{file_id}.jpg')
        os.system(
            f'python GFPGAN/inference_gfpgan.py -i bot/downloads/{file_id}.jpg -o bot/results -v 1.3 -s 4 --bg_upsampler realesrgan')
        await message.answer(LEXICON_RU['processed'])
        await message.answer_photo(
            FSInputFile(path=f"bot/results/restored_imgs/{file_id}.jpg"))
    else:
        await message.answer(LEXICON_RU['something_wrong'])
    USERS_UPSCALE_STATE[user_id] = False


@router.message(F.content_type != 'photo')
async def process_other_messages(message: Message):
    user_id = message.from_user.id
    USERS_UPSCALE_STATE[user_id] = False
    await message.answer(LEXICON_RU['incorrect_input'])
