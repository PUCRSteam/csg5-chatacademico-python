from typing import List

from app.models import Chat

from .repository import ChatRepository


class ChatService:

	@staticmethod
	def get(user_id: int, chat_id: int) -> Chat:
		return ChatRepository.get_by_id(user_id, chat_id)

	@staticmethod
	def get_all(user_id: int) -> List[Chat]:
		return {'data': ChatRepository.get_all(user_id)}

	@staticmethod
	def create(user1_id: int, user2_id: int) -> any:
		chat = Chat(
			user1_id=user1_id,
			user2_id=user2_id
		)
		return ChatRepository.create(chat)
