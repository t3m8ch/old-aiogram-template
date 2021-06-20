import logging

import uvloop
from aiogram import Dispatcher
from aiogram import executor

from loader import dp
from utils.commands import set_commands
from config import LOGGING_LEVEL, LOGGING_FORMAT, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT
import handlers

logging.getLogger(__name__)


async def on_startup(dp: Dispatcher):
    logging.warning("Starting bot...")

    await dp.bot.set_webhook(WEBHOOK_URL)
    await set_commands(dp.bot)  # TODO: Add admin notify


async def on_shutdown(dp: Dispatcher):
    logging.warning("Shutting down...")

    await dp.bot.delete_webhook()

    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning("Bye!")


if __name__ == "__main__":
    uvloop.install()
    logging.basicConfig(
        level=LOGGING_LEVEL,
        format=LOGGING_FORMAT
    )
    webhook_path = "/" + "/".join(WEBHOOK_URL.split("/")[3:])
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=webhook_path,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )

