import requests
from flask import Flask

from app.errors.client.base import UnauthorizedException


class MockedAuthService:

	def __init__(self, app:Flask=None):
		...

	def init_app(self, app: Flask):
		...

	def authenticate(self, token: str) -> dict:
		return {
			'user_id': 1
		}
