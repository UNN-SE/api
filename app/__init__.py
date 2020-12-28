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
service_repository = None
photostore_repository = None


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

    from .logic.order_repository import OrderRepositoryFolder, OrderRepositoryDB
    from .logic.user_repository import UserRepositoryMock, UserRepositoryDB
    from .logic.service_repository import ServiceRepositoryMock, ServiceRepositoryDB
    from .logic.photostore_repository import StoreRepositoryMock, StoreRepositoryDB
    global order_repository
    global user_repository
    global service_repository
    global photostore_repository
    if loc_app.config['NO_DB']:
        order_repository = OrderRepositoryFolder()
        user_repository = UserRepositoryMock()
        service_repository = ServiceRepositoryMock()
        photostore_repository = StoreRepositoryMock()
    else:
        order_repository = OrderRepositoryDB()
        user_repository = UserRepositoryDB()
        service_repository = ServiceRepositoryDB()
        photostore_repository = StoreRepositoryDB()
    from app import routes, models

    # db.create_all()
    return loc_app
