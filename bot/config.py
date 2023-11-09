from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 16970144))
    API_HASH = env.get("TELEGRAM_API_HASH", "9aaa8123d070b0507ebb24dac8443857")
    OWNER_ID = int(env.get("OWNER_ID", 969730932))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Yoko_Robot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "5479481991:AAHtca0jxG7Uqf5aeQTrpcd9Cb3TPC00QEQ")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002124550695))
    BOT_WORKERS = int(env.get("BOT_WORKERS", 10))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "34.216.12.78:56293")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "https://gloomlabsweb.run-us-west2.goorm.app")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'hypercorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hypercorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
