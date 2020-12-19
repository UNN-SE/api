import os
import tempfile


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '{H#DH0*Fs!7#R(Pfdwe2'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@localhost/my_db'
    NO_DB = os.environ.get("NO_DB", default="false").lower() in {"1", "t", "true"}
    PHOTOS_DIR = tempfile.gettempdir()
