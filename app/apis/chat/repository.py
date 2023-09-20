from sqlalchemy import or_
from typing import List
from app.ext.database import db
from app.models import Chat


class ChatRepository:
	
	@staticmethod
	def get_by_id(user_id: int, chat_id: int) -> Chat:
		return db.session.query(Chat).filter(
			or_(
				Chat.user1_id == user_id,
				Chat.user2_id == user_id
			),
			Chat.id == chat_id
		).first_or_404()
	
	@staticmethod
	def get_all(user_id: int) -> List[Chat]:
		return db.session.query(Chat).filter(
			or_(
				Chat.user1_id == user_id,
				Chat.user2_id == user_id
			)
		).all()
	
	@staticmethod
	def create(chat: Chat) -> Chat:
		db.session.add(Chat)
		db.session.commit()
		return chat
	