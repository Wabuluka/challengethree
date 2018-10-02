from flask import request
from flask_restful import Resource, Api
from app import app
from app.models.database import DatabaseConnection
# from flask_jwt import JWT, jwt_required
# from app.authentication import authenticate, identity
#app = Flask(__name__)

api = Api(app)
app.secret_key = 'dave'
# jwt = JWT(app, authenticate)
# orders = []

database = DatabaseConnection()

database.create_user_table()
database.create_menu_list()
cur = database.cursor

#getting all the orders from the database
@app.route('/orders')
def get_all_orders(self):
    
    
