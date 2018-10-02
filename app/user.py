from app.models.database import DatabaseConnection

database = DatabaseConnection()
database.create_user_table()
database.cursor

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def select_user_by_name(self, username):
        # database = DatabaseConnection()
        # database.create_user_table()
        # database.cursor

        query = "SELECT * from users WHERE username =?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user
