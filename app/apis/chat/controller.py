from flask_restx import Resource

from .dto import ChatDto
from .service import ChatService

ns = ChatDto.api

@ns.route('/<int:chat_id>')
class ChatController(Resource):

	@ns.marshal_list_with(ChatDto.example_model)
	def get(self, chat_id: int):
		return ChatService.get(chat_id)
