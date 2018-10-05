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
        try:
            query = "SELECT * FROM users WHERE username= %s AND password= %s"
            # query = "SELECT userId FROM users WHERE username = {} AND password = {}".format(
            #     username, password)
            # query = "SELECT * FROM users "
            cur.execute(query, (username, password))
            result = cur.fetchone()
            print(result)
            return result
        except Exception as error:

            print(str(error))
