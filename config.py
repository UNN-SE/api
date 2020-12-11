import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@localhost/my_db'