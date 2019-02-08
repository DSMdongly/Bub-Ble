from datetime import timedelta
import os


class Config:
    SERVICE_NAME = "Poem"
    DEBUG = False
    HOST = 'localhost'
    PORT = os.getenv("PORT", 5000)
    SECRET_KEY = os.getenv("SECRET_KEY", "PLEASE SET YOUR SECRET KEY")

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_HEADER_TYPE = "JWT"

    SWAGGER = {
        'title': SERVICE_NAME + ' API DOCS',
        'specs_route': 'docs',
        'uiversion': 3,

        'info': {
            'title': 'API Docs',
            'description': 'API Docs for ' + SERVICE_NAME,
            'version': '1.0.0',
        },

        'host': '{}:{}'.format(HOST, PORT),
        'basePath': '/',
    }

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


from config.dev import DevConfig
from config.test import TestConfig
from config.prod import ProdConfig