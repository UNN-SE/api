from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

log = app.logger

from .logic.order_repository import *

if app.config['TEST_MODE']:
    order_repository = OrderRepositoryFolder()

from app import routes, models
