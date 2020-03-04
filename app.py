from flask import Flask
from flask import request
# from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]

def create_app(config_name):
	app = Flask(__name__)

	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	@app.route('/')
	def index():
		user_agent = request.headers.get('User-Agent')
		return f'<p>Your browser is {user_agent}</p>'

	return app
