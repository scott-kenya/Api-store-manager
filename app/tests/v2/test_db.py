# import unittest
# import json
# from app import create_app
# from instance.config import app_config


# class Test_users(unittest.TestCase):

# 	@classmethod
# 	def setUpClass(self):
# 		"""Initializing the app"""
# 		self.app = create_user(app_config['testing'])
# 		self.test_client =self.app.test_client()
# 		self.app_context = self.app.app_context()
# 		self.app_context.push()

# 		 # binding the app to the current context
#         with self.app.app_context():
#             # create all tables
#             db.create_all()

#     	self.user={
#     		'name': 'scott francis',
#     		'email': 'scott@hotmail.com',
#     		'password': 'password',
#     		'role': 'admin'
#     	}


# 	@classmethod
# 	def tearDownClass(cls):
# 		pass

# 	def test_create_user_acount(self):
# 		"""POST request"""
# 		response = self.client().post('/auth/signup', data=self.user, content_type="applicatio/json")
#         self.assertEqual(response.status_code, 201)
        

# 	def test_signin_or_signout(self):
# 		return 

# 	def test_modify_product(self):
# 		v = self.client().post('/products/<productId> ',data=json.dumps({
# 			'name': 'vanilla',
# 			'price': 1200,
# 			'sale_id': 1,
# 			'quantity': 50,
# 			'createdby': 'Scott Duex'
# 			}))
#         self.assertEqual(rv.status_code, 201)
       
       
# 	def test_delete_product(self):
# 		v = self.client().post('/products/<productId> ',data=json.dumps({
# 			'name': 'vanilla',
# 			'price': 1200,
# 			'sale_id': 1,
# 			'quantity': 50,
# 			'createdby': 'Scott Duex'
# 			}))
#         self.assertEqual(rv.status_code, 201)

# 		 response = self.client().delete('/products/<productId>')
#         self.assertEqual(res.status_code, 200)
#         # If it exists, should return a 404
#         result = self.client().get('/products/<productId>')
#         self.assertEqual(result.status_code, 404)