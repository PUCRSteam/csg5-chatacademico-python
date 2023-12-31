from app.errors.base import ApiException


class ClientException(ApiException):
	code = 400


class BadRequestException(ClientException):
	code = 400


class UnauthorizedException(ClientException):
	code = 401

	def __init__(self, message: str=''):
		self.message = message


class ForbiddenException(ClientException):
	code = 404


class NotFoundException(ClientException):
	code = 404
	message = 'Not Found.'
	