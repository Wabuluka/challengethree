from app import app
from app.models.database import DatabaseConnection

database = DatabaseConnection()
# database.create_order_list()
# database.create_user_table()
#database.create_menu_list()
cur = database.cursor

class Orders():
    
    def get(self):
        query = "SELECT * FROM orders"
        cur.execute(query)
        result = cur.fetchall()
        return result

    def post(self, orderId, menuId, userId):
        query = "Insert INTO orders (orderId, menuId, userId) VALUES({},'{}','{}')".format(
            orderId, menuId, userId)
        cur.execute(query)

    def get_one_order(self, orderId):
        query = "SELECT * FROM orders WHERE orderId = '{}'".format(orderId)
        cur.execute(query)
        result = cur.fetchone()
        return result