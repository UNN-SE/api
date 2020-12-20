from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from config import Config
from flask_sqlalchemy import SQLAlchemy


LOG = None
APP = None
DB = None
AUTH = None
SERIALIZER = None
ORDER_REPOSITORY = None
USER_REPOSITORY = None


def create_app():
    loc_app = Flask(__name__)
    global APP
    APP = loc_app
    loc_app.config.from_object(Config)
    global LOG
    LOG = loc_app.logger
    CORS(loc_app)

    global AUTH
    AUTH = HTTPTokenAuth()
    global SERIALIZER
    SERIALIZER = Serializer(loc_app.config['SECRET_KEY'])

    global DB
    DB = SQLAlchemy(loc_app)

    from .logic.order_repository import OrderRepositoryFolder
    from .logic.user_repository import UserRepositoryMock
    global ORDER_REPOSITORY
    global USER_REPOSITORY
    if loc_app.config['NO_DB']:
        ORDER_REPOSITORY = OrderRepositoryFolder()
        USER_REPOSITORY = UserRepositoryMock()
    from app import routes, models

    return loc_app

