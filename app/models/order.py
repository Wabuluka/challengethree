from app import app
from app.models.database import DatabaseConnection

database = DatabaseConnection()
database.create_order_list()
# database.create_user_table()
#database.create_menu_list()
cur = database.cursor

class Orders():
    """Retreiving all the orders from the database"""
    def get(self, orderId, userId, menuId):
        query = "SELECT * FROM orders "
        cur.execute(query)
        result = cur.fetchall()
        return result

    def post(self, orderId, menuId, userId):
        query = "Insert INTO orders (orderId, menuId, userId) VALUES({},'{}','{}')".format(
            orderId, menuId, userId)
        cur.execute(query)
