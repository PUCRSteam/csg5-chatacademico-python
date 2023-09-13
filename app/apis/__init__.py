from flask import Flask

def init_apis(app: Flask, base_url: str):
	from .chat import inject_api as inject_chat_api
	
	inject_chat_api(app, f'{base_url}/chat')
	