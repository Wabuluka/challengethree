from app import app
from app.models.database import DatabaseConnection

database = DatabaseConnection()

# database.create_user_table()
database.create_menu_list()
cur = database.cursor

class User():
    """
        Handling users
    """
    def post(self, userId, username, password):
        query = "Insert INTO users (userId, username, password) VALUES({},'{}','{}')".format(
            userId, username, password)
        cur.execute(query)

    def signin(self, username, password):
        query = "SELECT username, password FROM users WHERE username = {} AND password ={}"
        cur.execute(query)
        result = cur.fetchone()
        return result