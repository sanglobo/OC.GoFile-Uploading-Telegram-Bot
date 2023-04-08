import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5836338648:AAG-zGTyl1ZcuJ8CMhDFlImrOIjxTSH1YQ0")

    APP_ID = int(os.environ.get("APP_ID", 27885485))

    API_HASH = os.environ.get("API_HASH", "7dd9974c713787410beae4a295cc1e2d")

