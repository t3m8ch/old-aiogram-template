import logging
from os import getenv


# Webhook
WEBHOOK_URL = getenv("WEBHOOK_URL")
assert WEBHOOK_URL is not None, "WEBHOOK_URL is not set"

WEBAPP_HOST = getenv("WEBAPP_HOST", "localhost")
WEBAPP_PORT = int(getenv("WEBAPP_PORT", 3000))

# Token
TG_TOKEN = getenv("TG_TOKEN")
assert TG_TOKEN is not None, "TG_TOKEN is not set"

TG_ADMIN_ID = getenv("TG_ADMIN_ID")
assert TG_ADMIN_ID is not None, "TG_ADMIN_ID is not set"

# Messages
PARSE_MODE = "MarkdownV2"

# Logging
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

# DB
REDIS_HOST = getenv("REDIS_HOST", "localhost")
REDIS_PORT = getenv("REDIS_PORT", 6379)
