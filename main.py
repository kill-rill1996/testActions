import asyncio

import aiogram as io
import requests
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings


# async def start_bot() -> None:
#     """Запуск бота"""
#     bot = io.Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#
#     storage = MemoryStorage()
#     dispatcher = io.Dispatcher(storage=storage)
#
#     dispatcher.include_routers(admin.router, users.router)
#
#     await dispatcher.start_polling(bot)
#

def send_message(message):

    url = f"https://api.telegram.org/bot{settings.bot_token}/sendMessage"

    params = {
        "chat_id": settings.chat_id,
        "text": message
    }
    print(params)
    res = requests.post(url, data=params)
    print(res.text)

    print(message)


if __name__ == "__main__":
    print("Запуск бота...")
    send_message("Hello from bot")