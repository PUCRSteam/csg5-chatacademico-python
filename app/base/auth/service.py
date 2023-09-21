import requests
from flask import Flask

from app.errors.client.base import UnauthorizedException


class AuthService:

	def __init__(self, app:Flask=None):
		self.api_url = ''
		if app is not None:
			self.init_app(app)

	def init_app(self, app: Flask):
		self.api_url = app.config.get('AUTH_SERVICE_API_URL')

	def authenticate(self, token: str) -> dict:
		data = {
			'token': token
		}
		res = requests.get(f'{self.api_url}/authenticate', data=data)

		if res.status_code not in [200, 201]:
			raise UnauthorizedException(res.json()['message'])
		
		return res.json()
