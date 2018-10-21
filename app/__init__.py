from flask import Flask, jsonify
from flask_restful import Api
from .api.v1.views import zed
from instance.config import app_config
from flask_jwt_extended import JWTManager
from flask_httpauth import HTTPBasicAuth

# def create_app(self):
# 	app = Flask(__name__)
	
# 	app.register_blueprint(zed)

# 	return app



def create_app(self):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    auth = HTTPBasicAuth()

    from app.api.v1 import zed

    # register the blueprint
    app.register_blueprint(zed)

    app.config['JWT_SECRET_KEY'] = 'jesusismylordandsavior'
    jwt = JWTManager(app)


    return app