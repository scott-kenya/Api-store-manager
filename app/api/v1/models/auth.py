# import string
# from flask import jsonify
# from werkzeug.security import generate_password_hash, check_password_hash

# users = {}

# class Users():
#     def __init__(self):
#         self.singleuser = {}

#     def put(self, name, username, email, password,role):
#         '''add a user to users'''
#         if username in users:
#             return {"message":"Username already exists"}
        
#         self.singleuser["name"] = name
#         self.singleuser["email"] = email
#         self.singleuser["username"] = username
#         self.singleuser["role"] = role
#         pw_hash = generate_password_hash(password)
#         self.singleuser["password"] = pw_hash

#         user[email] = self.singleuser
#         return {"message":"{} registered successfully".format(email)}

#     def verify_password(self, email, password):
#         '''verify the password a user enters while logging in'''
#         if email in users:
           
#             return "True"
            
#         return {"message": "email does not exist in our records"}
#     def get_user_by_email(self,email):
#         if email in users:
#             return users[email]
#         return {"message":"User not found"}