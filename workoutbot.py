from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.commands import command_router
from handlers.callback import callbacks_router
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.fsm import fsm_router
from antiflood import AntiFloodMiddleware
sorted


from dotenv import load_dotenv
import os

import asyncio


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
dp.include_router(command_router)
dp.include_router(callbacks_router)
dp.include_router(fsm_router)
dp.message.middleware(AntiFloodMiddleware())



async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())


