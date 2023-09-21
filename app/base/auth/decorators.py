from functools import wraps
from flask import g, request

from app.ext.auth import auth_service
from app.errors.client.custom import TokenMissingException

def token_required(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		token = None
		if "Authorization" in request.headers:
			token = request.headers["Authorization"].split(" ")[1]
		if not token:
			raise TokenMissingException()

		
		data = auth_service.authenticate(token)

		g.current_user_id = data.get('user_id')
		return func(*args, **kwargs)

	return wrapper