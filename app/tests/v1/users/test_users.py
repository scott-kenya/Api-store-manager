# import unittest
# import json
# from app import create_app
# from instance.config import app_config
# import datetime


# class Test_create_users(unittest.TestCase):

#     @classmethod
#     def setUpClass(self):
#         self.app = create_app(app_config['testing'])
#         self.test_client = self.app.test_client()
#         self.app_context = self.app.app_context()
#         self.app_context.push()

#     def test_register_users(self):
#         data = json.dumps({
#             'username': 'scott',
#              'email': 'scott@gmail.com',
#              'password': 'jesusislord',
#              'user_id': 1
#          })
        

#         response = self.test_client.post(
#             '/api/v1/createUsers', data=data, content_type="application/json")
#         self.assertEqual(response.status_code, 201)

#     def test_get_users(self):
#         response = self.test_client.get(
#             '/api/v1/createUsers', content_type="application/json")
#         self.assertEqual(response.status_code, 200)