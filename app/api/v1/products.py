from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api, reqparse

#from app.api.models import products

products = []

class Products(Resource):
	
	def get(self):
		"""Endpoint for fetching all products"""
		return jsonify(products)
		return jsonify({'message':'Item not found'},
						{'status': 200}
			)



