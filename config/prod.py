from config import Config
import os


class ProdConfig(Config):
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('HEROKU_POSTGRES_URL')