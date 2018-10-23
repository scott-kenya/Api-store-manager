from flask import Flask, make_response, jsonify, request, abort, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
from flask_httpauth import HTTPBasicAuth


products = []
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "SuperSecretPwd"
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class Products(Resource):
	@auth.verify_password
	def get(self):
		"""Endpoint for fetching all products"""
		return jsonify(products)
		return jsonify({'message':'Item not found'},{'status': 200})

	@auth.verify_password
	def post(self):
		"""Endpoint for adding new pdt"""
		data = request.get_json()
		if not data:
			return jsonify({"message": "You cannot leave this empty"})
		name = 'name'
		price = 'price'
		Product_id = len(products)+1
		quantity = 'quantity'
		createdby = 'createdby'
		if not name or name == "":
			return jsonify({"message": "Please enter product name"}), 404
		if not price or price == "":
			return jsonify({"message": "Please enter value"}), 404
		if not Product_id or Product_id == "":
			return jsonify({"message": "Please enter valid id"}), 404
		if not quantity or quantity == "":
			return jsonify({"message": "Please enter value"}), 404
		else:

			sal = {
			'name': data['name'],
			'price': data['price'],
			'Product_id': len(products)+1,
			'quantity': data['quantity']
			}

			products.append(sal)
			
			return make_response(jsonify({'list': products}),201)


class Product_id(Resource):
	@auth.verify_password
	def get(self, product_id):
		product = [product for product in products if product['product_id'] == Product_id] or None
		if product:
			return jsonify({'product':product[0]})
		else:
			return jsonify({'message': "item not found"})
		return 404

	@auth.verify_password
	def delete(self, sale_id):
		product = [product for product in products if product['product_id'] == product_id] or None

		if product:
			return jsonify({'message':'Item deleted'})
		else:
			return jsonify({'message': "item not found"})
		return 404

