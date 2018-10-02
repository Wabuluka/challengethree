from app import app
from app.models.database import DatabaseConnection

database = DatabaseConnection()

database.create_user_table()
# database.create_menu_list()
cur = database.cursor

class Users():
    def post(self, userId, username, password):
        query = "INSERT INTO users (userId, username, password) VALUES({},'{}','{}')".format(
            userId, username, password)
        cur.execute(query)

    def get(self, userId, username, password):
        query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
        cur.execute(query)
        return cur.fetchone()
        