from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api, reqparse



products = []

class Products(Resource):
	
	def get(self):
		"""Endpoint for fetching all products"""
		return jsonify(products)
		return jsonify({'message':'Item not found'},{'status': 200})

	
	def post(self):
		"""Endpoint for adding new pdt"""
		data = request.get_json()
		if not data:
			return jsonify({"message": "You cannot leave this empty"})
		name = 'name'
		price = 'price'
		product_id = len(products)+1
		quantity = 'quantity'
		
		if not name or name == "":
			return jsonify({"message": "Please enter product name"}), 404
		if not price or price == "":
			return jsonify({"message": "Please enter value"}), 404
		if not product_id or product_id == "":
			return jsonify({"message": "Please enter valid id"}), 404
		if not quantity or quantity == "":
			return jsonify({"message": "Please enter value"}), 404
		
		else:

			payload = {
			'name': data['name'],
			'price': data['price'],
			'product_id': len(products)+1,
			'quantity': data['quantity'],
			
			}

			products.append(payload)
			
			return make_response(jsonify({'list': products}),201)

		
class Product_id(Resource):

	def get(self, product_id):
		product = [product for product in products if product['product_id'] == product_id] or None
		if product:
			return jsonify({'product':product[0]})
		else:
			return jsonify({'message': "item not found"})
		return 404
 