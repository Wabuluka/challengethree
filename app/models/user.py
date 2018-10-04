from app import app
from app.models.database import DatabaseConnection

database = DatabaseConnection()

database.create_user_table()
database.create_menu_list()
cur = database.cursor

class Users():
    def post(self, userId, username, userRole, password):
        query = "INSERT INTO users (userId, username,userRole, password) VALUES('{}','{}','{}','{}')".format(
            userId, username, userRole, password)
        cur.execute(query)

    def get(self, username, password):
        query = "SELECT * FROM users WHERE"
        cur.execute(query, (username, password))
        return cur.fetchone()
        
