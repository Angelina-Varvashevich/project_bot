import asyncio

from aiogram import Bot, Dispatcher
from bot.config_data.config import Config, load_config
from bot.handlers import user_handlers

async def main():
    config: Config = load_config()
    bot = Bot(token=config.telegram_bot.token, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
