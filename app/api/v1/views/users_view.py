import datetime

from flask import jsonify, make_response, request
from flask_restful import Resource
from instance.config import Config
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

from app.api.v1.views.utils import Utils


users = []

class Register(Resource):
	def post(self):
		data = request.get_json()
		self.email = data['email']
		self.username = data['username']
		self.password = data['password']
		self.Repeat_password = data['Repeat_password']
		self.role = data['role']

		for user in users:
			if user["email"] ==self.email:
				return "user already exists"

			if user["username"] ==self.username:
				return "username already exists"


		id = len(users) + 1


		user = {
			"email": self.email,
			"username": self.username,
			"password": self.password,
			"Repeat_password": self.Repeat_password,
			"role": self.role
		}

		users.append(user)
		return make_response(jsonify(
			{
				"Message": "User successfully created",
				"User": users
			}), 201)
class  LoginUser(Resource):
	"""docstring for  LoginUser"""
	def post(self):
		data = request.get_json()
		self.email = data['email']
		self.password = data['password']

		for user in users:
			if user['email'] == self.email and user['password'] == self.password:
				access_token = create_access_token(identity="email", expires_delta=datetime.timedelta(minutes=50))
				refresh_token = create_refresh_token(identity="email")
				return make_response(jsonify({
					"Message": "Login successful",
					"access_token": access_token,
					"refresh_token": refresh_token
					}))
			else:
				return {'Message': 'wrong credentials'},400


