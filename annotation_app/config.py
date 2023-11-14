"""Flask app configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = 'wsgi.py'

    SECRET_KEY = environ.get('SECRET_KEY')

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_PROD_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    FLASK_ENV = environ.get('FLASK_ENV')

    LESS_BIN = '/usr/local/bin/lessc'
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DEV_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
