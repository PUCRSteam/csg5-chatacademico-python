from flask import Flask
from flask_sqlalchemy.query import Query

from app.errors.base import ApiException
from app.ext.database import db
from app.ext.cors import cors
from app.ext.migration import migrate
from app.ext.socketio import socketio
from app.ext.errorhandler import api_exception_handler
from app.ext.modifiers import make_notfound_handling
from app.ext.auth import auth_service


def init_extensions(app: Flask):
	
	make_notfound_handling(Query)

	db.init_app(app)
	migrate.init_app(app, db)
	app.register_error_handler(ApiException, api_exception_handler)
	cors.init_app(app)
	auth_service.init_app(app)
	socketio.init_app(app)
	