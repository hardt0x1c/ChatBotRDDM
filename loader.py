import logging
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from config import *
from data.database.DatabaseManager import DatabaseManager

logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher()
db = DatabaseManager('data/database/database.db')
