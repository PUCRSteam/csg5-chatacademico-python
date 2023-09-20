from datetime import datetime

from app.models import Message

from .repository import MessageRepository


class MessageService:

	@staticmethod
	def create(chat_id: int, payload: dict) -> any:
		message = Message(
			chat_id=chat_id,
			sender_user_id=payload.get('sender_user_id'),
			content=payload.get('content'),
			date=datetime.now()
		)
		return MessageRepository.create(message)
		