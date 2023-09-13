from flask import Flask, Blueprint
from flask_restx import Api

def inject_api(app: Flask, path: str):

	blueprint = Blueprint('bp_api_chat', __name__)
	chat_api = Api(blueprint, title='Chat REST API')

	from .controller import ns
	chat_api.add_namespace(ns)

	app.register_blueprint(blueprint, url_prefix=path)
