from flask_restx import Namespace, fields


class ChatDto:
	api = Namespace(name='Chat', description='Operations related to chat.')

	example_model = api.model(
		'example_model',
		{
			'id': fields.Integer(),
			'name': fields.String(),
			'example': fields.String()
		}
	)
