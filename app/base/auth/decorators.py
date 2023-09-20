from functools import wraps
from flask import g


def token_required(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		g.current_user_id = 1
		#TODO temp
		g.user_name = 'bini'
		return func(*args, **kwargs)

	return wrapper