import unittest
import json
from app import create_app
from ...instance.config import app_config


class Test_products(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.app = create_app(app_config['testing'])
		self.test_client =self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()


	def test_post_products(self):
		""" dummy data"""
		data = json.dumps({
			"name": "vanilla",
			"price": 1500,
			"product_id": 1,
			"quantity": 20
			})
		self.create_sales= json.dumps({
			"id": "1",
			})
		response = self.test_client.post('/api/v1/products', data = data, content_type="application/json")
		self.assertEqual(response.status_code, 201)

	def test_get_products(self):
		response = self.test_client.get('/api/v1/products', content_type="application/json")
		self.assertEqual(response.status_code, 200)
	
	def test_get_products_by_id(self):
		response = self.test_client.get('/api/v1/products/1',content_type="application/json")
		self.assertEqual(response.status_code, 200)

	def test_post_sales(self):
		""" dummy data"""
		data = json.dumps({
			"id": "1",
			})
		response = self.test_client.post('/api/v1/sales', data = data, content_type="application/json")
		self.assertEqual(response.status_code, 201)




	def test_get_sales(self):
		response = self.test_client.get('/api/v1/sales', content_type="application/json")
		self.assertEqual(response.status_code, 200)
		