from datetime import datetime

from app.ext.database import db


class Message(db.Model):
	__tablename__ = 'messages'

	id: int = db.Column(db.Integer, primary_key=True)

	chat_id: int = db.Column(
        db.Integer, db.ForeignKey('chats.id', ondelete='CASCADE'), nullable=False
    )

	chat = db.relationship('Chat', backref='messages')#lazy="joined"

	sender_user_id: int = db.Column(db.Integer, nullable=False)

	content: int = db.Column(db.String(1024), nullable=False)

	date: datetime = db.Column(db.DateTime(), default=datetime.utcnow)
