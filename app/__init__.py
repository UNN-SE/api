from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

log = app.logger

from .logic.order_repository import *

if app.config['NO_DB']:
    order_repository = OrderRepositoryFolder()

db = SQLAlchemy(app)

from app import routes, models