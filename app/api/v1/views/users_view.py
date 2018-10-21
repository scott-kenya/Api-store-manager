# import re
# from flask import request, jsonify
# from flask_restful import Resource
# from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
# from ..models import auth

# the_list = auth.Users()


# class Login(Resource):
#     """login in registered users returns token and confirmation message """
#     def post(self):
#         data = request.get_json()
#         if not data:
#             return jsonify({"message": "Email and password required"})

#         email = data.get('email')
#         password = data.get('password')

#         if not email or not password:
#             return jsonify({"message": "Username or password missing"})

#         authorize = the_list.verify_password(email, password)
#         user=the_list.get_user_by_email(email)

#         if authorize:
#             access_token = create_access_token(identity=user)
#             return jsonify(token = access_token, message = "Login successful!")
        
        
        
# class Register(Resource):
#     """register new users """

#     def post(self):
#         data = request.get_json()

#         # users input
#         name = data.get('name')
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         # confirm_password = data['confirm_password']
#         role=data.get('role')

#         roles=["owner","admin","attendant"]
        
#         if role not in roles:
#             return jsonify({"message":"The role {} does not exist".format(role)})
       
#         # check email format
#         email_format = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

#         # check validity of email 
#         if email_format is None:
#             return jsonify({"message": "invalid email address"})

#         # if password is not confirm_password:
#             # return jsonify({'message':'passwords do not match'})

#         response = jsonify(the_list.put(name, username, email, password,role))
#         response.status_code = 201
#         return response