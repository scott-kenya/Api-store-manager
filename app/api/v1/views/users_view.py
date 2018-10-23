from flask import jsonify, make_response, request
from flask_restful import Resource
from instance.config import Config


users = []

class Register(Resource):
	def post(self):
		data = request.get_json()
		self.email = data['email']
		self.password = data['password']
		self.role = data['role']

		for user in users:
			if user["email"] ==self.email:
				return "user already exists"
		id = len(users) + 1


		user = {
			"email": self.email,
			"password": self.password,
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
				return make_response(jsonify({
					"Message": "Login successful"
					}))