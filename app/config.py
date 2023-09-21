import os

from flask import Flask


def getenv(name, required=True):
	try:
		return os.environ[name]
	except KeyError:
		if required:
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
	SECRET_KEY = 'Ch4v3Sup3rS3c3t4*12'

	AUTH_SERVICE_API_URL = getenv('AUTH_SERVICE_API_URL', required=False)


class DevelopmentConfig(Config):
	FLASK_DEBUG = 1


def init_config(app: Flask):
    #! TEMP
	config = DevelopmentConfig()
	app.config.from_object(config)
      