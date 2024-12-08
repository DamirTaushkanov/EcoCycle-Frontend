import asyncio
import logging
import os
import sys

import dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.router import router
from handlers import register

dotenv.load_dotenv()

# Создаем объекты бота и диспетчера
bot = Bot(token=os.getenv("API_TOKEN"))
dp = Dispatcher(storage=MemoryStorage())

async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())