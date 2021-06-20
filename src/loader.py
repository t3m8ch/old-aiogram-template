from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage

from config import TG_TOKEN, PARSE_MODE, REDIS_HOST, REDIS_PORT

bot = Bot(token=TG_TOKEN, parse_mode=PARSE_MODE)
storage = RedisStorage(REDIS_HOST, REDIS_PORT)
dp = Dispatcher(bot, storage=storage)
