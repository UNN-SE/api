from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy


log = None
app = None
db = None
order_repository = None


def create_app():
    loc_app = Flask(__name__)
    global app
    app = loc_app
    loc_app.config.from_object(Config)
    CORS(loc_app)
    global log
    log = loc_app.logger

    from .logic.order_repository import OrderRepositoryFolder
    global order_repository
    if loc_app.config['NO_DB']:
        order_repository = OrderRepositoryFolder()
    global db
    db = SQLAlchemy(app)
    from app import routes, models

    return loc_app
