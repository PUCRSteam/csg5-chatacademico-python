from app.ext.database import db
from app.models import Message


class MessageRepository:
	
	@staticmethod
	def create(message: Message) -> Message:
		db.session.create(Message)
		db.session.commit()
		return message
