from app.ext.database import db

from .repository import ChatRepository


class ChatService:

	@staticmethod
	def get(chat_id: int) -> any:
		...
