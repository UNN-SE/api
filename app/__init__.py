from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from config import Config
from flask_sqlalchemy import SQLAlchemy


log = None
app = None
db = None
auth = None
serializer = None
order_repository = None
user_repository = None


def create_app():
    loc_app = Flask(__name__)
    global app
    app = loc_app
    loc_app.config.from_object(Config)
    global log
    log = loc_app.logger
    CORS(loc_app)

    global auth
    auth = HTTPTokenAuth()
    global serializer
    serializer = Serializer(loc_app.config['SECRET_KEY'], expires_in=12*3600)

    global db
    db = SQLAlchemy(loc_app)

    from .logic.order_repository import OrderRepositoryFolder
    from .logic.user_repository import UserRepositoryMock, UserRepositoryDB
    global order_repository
    global user_repository
    if loc_app.config['NO_DB']:
        order_repository = OrderRepositoryFolder()
        user_repository = UserRepositoryMock()
    else:
        order_repository = OrderRepositoryFolder()  # TODO mock, remove it
        user_repository = UserRepositoryDB()
    from app import routes, models

    # db.create_all()
    return loc_app
