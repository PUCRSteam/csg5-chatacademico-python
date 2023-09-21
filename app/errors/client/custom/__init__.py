from app.errors.client.base import UnauthorizedException


""" UnauthorizedExceptions """
class TokenMissingException(UnauthorizedException):
	message = 'Token is missing.'
