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
    CORS(loc_app)
    global log
    log = loc_app.logger
    global auth
    auth = HTTPTokenAuth()
    global serializer
    serializer= Serializer(app.config['SECRET_KEY'])
    
    from .logic.order_repository import *
    from .logic.user_repository import *
    global order_repository
    global user_repository
    if loc_app.config['NO_DB']:
        order_repository = OrderRepositoryFolder()
        user_repository = UserRepositoryMock()
        
    global db
    db = SQLAlchemy(app)
    from app import routes, models

    return loc_app
