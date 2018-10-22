from flask import Flask, Blueprint
from flask_restful import Api, Resource
from app.api.v1.views.products import Products, Product_id
from app.api.v1.views.sales import Sales, Sale_id
from app.api.v1.views.users_view import Register
from app.api.v1.views.users_view import LoginUser
zed = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(zed)

api.add_resource(Products, '/products')
api.add_resource(Product_id, '/products/<int:product_id>')
api.add_resource(Sales, '/sales')
api.add_resource(Sale_id, '/sales/<int:sale_id>')
api.add_resource(Register, '/auth/register')
api.add_resource(LoginUser, '/auth/login')
