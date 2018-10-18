from flask import Flask
from flask_restful import Api
from .api.v1.views import zed
from instance.config import app_config

def create_app(self):
	app = Flask(__name__)
	
	app.register_blueprint(zed)

	return app