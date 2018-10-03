from app.models.database import DatabaseConnection
"""
    performing on the database
"""
database = DatabaseConnection()
database.cursor

# @app.route('/')
# def contacts():
#     try:
#         cursor.execute("""SELECT from salesforce.contact""")
#         rows = cur.fetchall()
#         response = ''
#         my_list = []
#         for row in rows:
#             my_list.append(row[0])