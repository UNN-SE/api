from flask import Flask
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

log = app.logger

from .logic.order_repository import *

if app.config['NO_DB']:
    order_repository = OrderRepositoryFolder()

from app import routes, models
