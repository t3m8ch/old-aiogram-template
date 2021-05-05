from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = []  # Add your commands here.
    await bot.set_my_commands(commands)
