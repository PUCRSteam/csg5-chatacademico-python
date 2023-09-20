from app.ext.database import db


class Chat(db.Model):
	__tablename__ = 'chats'

	__table_args__ = (db.UniqueConstraint('user1_id', 'user2_id'), )

	id: int = db.Column(db.Integer, primary_key=True)

	user1_id: int = db.Column(db.Integer, unique=True, nullable=False)

	user2_id: int = db.Column(db.Integer, nullable=False)
