from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api, reqparse

#from app.api.models import products

sales = []

class Sales(Resource):
	
	def get(self):
		"""Endpoint for fetching all products"""
		return jsonify(sales)
		return jsonify({'message':'Item not found'},
						{'status': 200}
			)

	
	def post(name):
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

		
