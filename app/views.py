from flask import request, jsonify
from flask_restful import Resource, Api
from app import app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from app.models.database import DatabaseConnection
# from flask_jwt import JWT, jwt_required
# from app.authentication import authenticate, identity
#app = Flask(__name__)
from app.models.order import Orders
from app.models.menu import Menu
from app.user import User

#
app.config['SECRET_KEY'] = 'secret' 
jwt = JWTManager(app)

api = Api(app)


database = DatabaseConnection()
order = Orders()
menu = Menu()
user = User()

database.create_user_table()
database.create_menu_list()
cur = database.cursor

"""
    Handling the order endpoints
"""
# #getting all the orders from the database
# @app.route('/orders', methods=['GET'])
# def get_all_orders():
#     response = order.get()
#     return jsonify({'orders': response})

# # @jwt_required
# @app.route('/orders/<int:orderId>', methods =['GET'])
# def get_one_order(orderId):
#     response = order.get_one_order(orderId)
#     return jsonify({'order': response})


# @app.route('/orders/<int:orderId>', methods=['POST'])
# @jwt_required
#     # Access the identity of the current user with get_jwt_identity  
# def create_order(orderId):
#     current_user = get_jwt_identity()
#     data = request.get_json()
#     orderId = data['orderId']
#     menuId = data['menuId']
#     userId = data['userId']
#     insert_user= order.post(orderId, menuId, userId)
#     return jsonify({'order': insert_user})




# """
#     Handling the menu endpoints
# """
# @app.route('/menu', methods=['POST'])
# def create_item():
#     data = request.get_json()    
#     menuId = data['menuId']
#     menuItem = data['menuItem']
#     menuDescription = data['menuDescription']
#     insert = menu.post(menuId, menuItem, menuDescription)
#     return jsonify({'Menu Item created': insert}), 201

# @app.route('/menu', methods=['GET'])
# def get_menu_items():
#     response = menu.get()
#     return jsonify({'order': response})


# """
#     Handling user end points
# """
# @app.route('/auth/signup', methods = ['POST'])
# def create_new_user():
#     data = request.get_json()
#     userId = data['userId']
#     username = data['username']
#     password = data['password']
#     insert = user.post(userId, username, password)
#     return jsonify({'Menu Item created': insert})

# @app.route('/auth/signin', methods=['POST'])
# def create_signin():
#     data = request.get_json()
#     username = data['username']
#     password = data['password']

#     select_user = user.signin(username, password)
#     # Identity can be any data that is json serializable
#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token), 200
    