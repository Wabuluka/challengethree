from flask import Flask
from app import app
from app.models.database import DatabaseConnection
db = DatabaseConnection()


db.create_menu_list()
db.create_order_list()
db.create_user_table()

if __name__ == '__main__':
    app.run(debug=True)
