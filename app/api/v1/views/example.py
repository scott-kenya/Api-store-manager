from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource

users = []



class Register(Resource):
	def post(self, email, password):
		self.email = email
		self.password = password

		data = request.get_json()

		id = len(users) + 1
		email = data["email"]
		password = data["password"]
		users.append()





	