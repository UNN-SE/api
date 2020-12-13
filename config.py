import os, tempfile

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345'

    PHOTOS_DIR = tempfile.gettempdir()
    TEST_MODE = True