from dataclasses import dataclass
from environs import Env

@dataclass
class TelegramBot:
    token: str

@dataclass
class Config:
    telegram_bot: TelegramBot

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(telegram_bot=TelegramBot(token=env('BOT_TOKEN')))
