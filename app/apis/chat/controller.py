from flask import g
from flask_restx import Resource

from app.base.auth.decorators import token_required
from .dto import ChatDto
from .service import ChatService

ns = ChatDto.api


@ns.route('')
class ChatCreateController(Resource):

	@ns.expect(ChatDto.chat_create_schema)
	@ns.marshal_with(ChatDto.chat_schema)
	@token_required
	def post(self):
		"""
		Create a chat
		"""
		return ChatService.create(**ns.payload)


@ns.route('')
class ChatController(Resource):

	@ns.marshal_with(ChatDto.wrapped_chat_list_schema)
	@token_required
	def get(self):
		"""
		Get all user chats.
		"""
		return ChatService.get_all(g.current_user_id)


@ns.route('/<int:chat_id>')
class ChatItemController(Resource):

	@ns.marshal_list_with(ChatDto.chat_schema)
	@token_required
	def get(self, chat_id: int):
		"""
		Get all messages from a chat and connect to room
		"""
		return ChatService.get(g.current_user_id, chat_id)
