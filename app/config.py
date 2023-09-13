import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask

load_dotenv(join(dirname(__file__), '.env'))

def getenv(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


class Config:
	DB_ENGINE = getenv('DB_ENGINE')
	DB_HOST = getenv('DB_HOST')
	DB_USERNAME = getenv('DB_USERNAME')
	DB_PASSWORD = getenv('DB_PASSWORD')
	DB_PORT = getenv('DB_PORT')
	DB_NAME = getenv('DB_NAME')

	SQLALCHEMY_DATABASE_URI = f'{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class LocalConfig():
    SQLALCHEMY_DATABASE_URI = f'sqlite:///database.db'


class DevelopmentConfig(Config):
	FLASK_DEBUG = 1


def init_config(app: Flask):
    #! TEMP
	config = LocalConfig()
	app.config.from_object(config)
      