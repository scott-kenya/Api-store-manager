from flask import jsonify, make_response, request
from flask_restful import Resource
from instance.config import Config
import jwt
from functools import wraps
from app.api.v1.models.user import User, users


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_obj = User()
        token = None
        current_user = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({
                'Message': 'Token is missing, You must login first'
            }), 401)
        try:
            data = jwt.decode(token, app_config['development'].SECRET_KEY, algorithms=['HS256'])

            for user in users:
                if user['username'] == data['username']:
                    current_user = user
        except Exception as e:
            print(e)
            return make_response(jsonify({'Message': 'Token is invalid'}),
                                 403)
        return f(current_user, *args, **kwargs)
    return decorated


class Register(Resource):
	def post(self):
		data = request.get_json()
		self.email = data['email']
		self.password = data['password']
		self.role = data['role']

		for user in users:
			if user["email"] == self.email:
				return "user already exists"

		id = len(users) + 1

		user = {
			"email": self.email,
			"password": self.password,
			"role": self.role
		}

		users.append(user)
		return make_response(jsonify(
			{
				"Message": "User successfully created",
				"User": users
			}), 201)


class LoginUser(Resource):
	"""docstring for  LoginUser"""
	@token_required
	def post(self):
		data = request.get_json()
		self.email = data['email']
		self.password = data['password']

		for user in self.user_obj:
			if user['username'] == username and check_password_hash(user["password"], password):
				token = jwt.encode({'username': user['username'], 'exp': datetime.datetime.utcnow() +
		                                    datetime.timedelta(minutes=3000)},
		                                   app_config['development'].SECRET_KEY, algorithm='HS256')
		                return make_response(jsonify({'token': token.decode('UTF-8')}), 200)
		                return token


class UserLogoutAccess(Resource):
	def user_logout(self, token):
	    """Method to logout a user"""
	    response = self.client().post(
	        '/api/v1/auth/logout',
	        headers=dict(Authorization='Bearer ' + token))
	    return response

	    def get_user_token(self):
	        """Get user token"""
	        auth_response = self.register_user('tester', 'test@gmail.com', 'test1234', 'test1234')
	        return json.loads(auth_response.data.decode())['access_token']
