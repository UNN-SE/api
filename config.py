import os
import tempfile


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345'

    NO_DB = os.environ.get("NO_DB", default="false").lower() in {"1", "t", "true"}
    PHOTOS_DIR = tempfile.gettempdir()