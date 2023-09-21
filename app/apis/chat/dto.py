from flask_restx import Namespace, fields


class ChatDto:
	api = Namespace(name='Chat', description='Operations related to chat.')

	chat_create_schema = api.model(
		'chat_create_schema',
		{
			'user1_id': fields.Integer(),
			'user2_id': fields.Integer()
		}
	)

	message_schema = api.model(
		'message_schema',
		{
			'id': fields.Integer(),
			'sender_user_id': fields.Integer(),
			'content': fields.String(),
			'date': fields.DateTime()
		}
	)

	chat_schema = api.model(
		'chat_schema',
		{
			'id': fields.Integer(),
			'user1_id': fields.Integer(),
			'user2_id': fields.Integer(),
			'messages': fields.List(fields.Nested(message_schema))
		}
	)

	chat_list_schema = api.model(
		'chat_list_schema',
		{
			'id': fields.Integer(),
			'user1_id': fields.Integer(),
			'user2_id': fields.Integer()
		}
	)

	wrapped_chat_list_schema = api.model(
		'wrapped_chat_list_schema',
		{
			'data': fields.List(fields.Nested(chat_list_schema))
		}
	)

	# message_list_schema = api.model(
	# 	'message_list_schema',
	# 	{
	# 		'messages': fields.List(fields.Nested(message_schema))
	# 	}
	# )
