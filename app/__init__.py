from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
auth = HTTPTokenAuth()
serializer = Serializer(app.config['SECRET_KEY'])

log = app.logger

from .logic.order_repository import *
from .logic.user_repository import *

if app.config['NO_DB']:
    order_repository = OrderRepositoryFolder()
    user_repository = UserRepositoryMock()

from app import routes, models