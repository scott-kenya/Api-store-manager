from flask import Flask, make_response, jsonify, request, abort, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
from flask_httpauth import HTTPBasicAuth


sales = []
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "SuperSecretPwd"
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password



class Home(Resource):
	"""docstring for home"""
	def get():
		return jsonify({"message": "Welcome to store manager"})

class Sales(Resource):
	@auth.verify_password
	def get(self):
		"""Endpoint for fetching all products"""
		return jsonify(sales)
		return jsonify({'message':'Item not found'},{'status': 200})

	@auth.verify_password
	def post(self):
		"""Endpoint for adding new pdt"""
		data = request.get_json()
		if not data:
			return jsonify({"message": "You cannot leave this empty"})
		name = 'name'
		price = 'price'
		sale_id = len(sales)+1
		quantity = 'quantity'
		createdby = 'createdby'
		if not name or name == "":
			return jsonify({"message": "Please enter product name"}), 404
		if not price or price == "":
			return jsonify({"message": "Please enter value"}), 404
		if not sale_id or sale_id == "":
			return jsonify({"message": "Please enter valid id"}), 404
		if not quantity or quantity == "":
			return jsonify({"message": "Please enter value"}), 404
		if not createdby or createdby == "":
			return jsonify({"message": "Please enter name"}), 404
		else:

			sal = {
			'name': data['name'],
			'price': data['price'],
			'sale_id': len(sales)+1,
			'quantity': data['quantity'],
			'createdby': data['createdby']
			}

			sales.append(sal)
			
			return make_response(jsonify({'list': sales}),201)


class Sale_id(Resource):
	@auth.verify_password
	def get(self, sale_id):
		sale = [sale for sale in sales if sale['sale_id'] == sale_id] or None
		if sale:
			return jsonify({'sale':sale[0]})
		else:
			return jsonify({'message': "item not found"})
		return 404

	@auth.verify_password
	def delete(self, sale_id):
		sale = [sale for sale in sales if sale['sale_id'] == sale_id] or None
		if sale:
			return jsonify({'message':'Item deleted'})
		else:
			return jsonify({'message': "item not found"})
		return 404
 	