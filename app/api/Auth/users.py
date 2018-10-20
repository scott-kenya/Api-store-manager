from flask import Flask, jsonify, request, make_response
import jwt
import datatime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ilovejesus'

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token =request.args.get('token')

		if not token:
			return jsonify({'message': 'Token is missing'}), 403

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])

		except:
			return jsonify({'message': 'Token is invalid'}), 403
		return f(*args, **kwargs)

	return decorated


@app.route('/unprotected')
def unprotected():
	return jsonify({'message': 'free'})

@app.route('/protected')
@token_required 
def protected():
	return jsonify({'message': 'This is only available to authorized personnel'})

@app.route('/login')
def login():
	auth = request.authorization

	if auth and auth.password == 'password':
		token = jwt.encode({'user':auth.username, 'exp': datatime.datatime.utcnow() +
			datatime.timedelta(minutes=45)},app.config['SECRET_KEY'] )

		return jsonify({'token': token.decode('UTF-8')})

	return make_response('could not verify!', 401, 
		{'WWW.Authenticate': 'Basic realm="login Required"'})

if __name__ == '__main__':
	app.run()



	# def token_required(func):
	# @wraps(func)
	# def decorated(*args, **kwargs):
	# 	token = None
	# 	if 'x-access-token' in request.headers:
	# 		token = request.headers['x-access-token']

	# 	if not token:
	# 		return make_response(jsonify({
	# 			"message":"the access token is missing,login"}, 401))

	# 	try:
	# 		data = jwt.decode(token, app.config['SECRET_KEY'])
	# 		for user in users:
	# 			if user['email'] == data['email']:
	# 				current_user = user

	# 	except:
	# 		print(config.SECRET_KEY)
	# 		return make_response(jsonify({"message": "This token is invalid"}, 403))

	# 	return func(current_user, *args, **kwargs)
	# return decorated


# 	class UserRegistration(Resource):
#     def post(self):
#         return jsonify({'message': 'User registration'})


# class UserLogin(Resource):
#     # def post(self):
#     #     return jsonify({'message': 'User login'})
#     def login(self):
#     	auth = request.authorization

# 	if auth and auth.password == 'password':
# 		token = jwt.encode({'user':auth.username, 'exp': datatime.datatime.utcnow() +
# 			datatime.timedelta(minutes=45)},app.config['SECRET_KEY'] )

# 		return jsonify({'token': token.decode('UTF-8')})

# 	return make_response('could not verify!', 401, 
# 		{'WWW.Authenticate': 'Basic realm="login Required"'})