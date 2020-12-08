import os
from flask import Flask
from flask_sqlalchemy.utils import sqlalchemy_version
import sqlalchemy
from sqlalchemy.engine import create_engine
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345'
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql+psycopg2://root:pass@localhost/my_db') or \
        'postgresql:///' + os.path.join(basedir, 'app.db')