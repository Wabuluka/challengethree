from app import app
from app.models.database import DatabaseConnection

database = DatabaseConnection()

# database.create_user_table()
database.create_menu_list()
cur = database.cursor

# class Menu():
#     """
#     fetching all menu items
#     """

#     def get(self):
#         query = "SELECT * FROM menu "
#         cur.execute(query)
#         result = cur.fetchall()
#         return result

#     def post(self, menuId, menuItem, menuDescription):
#         query = "Insert INTO menu (menuId, menuItem, menuDescription) VALUES({},'{}','{}')".format(
#             menuId, menuItem, menuDescription)
#         cur.execute(query)

#     def put(self, menuId, menuItem, menuDescription):
#         query = "UPDATE menu set menuItem = {}, menuDescription = {}".format(menuItem,menuDescription)
#         cur.execute(query)
#         result = cur.fetchall()
#         return result
