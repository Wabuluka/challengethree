import unittest
from app import app
from app.models.database import DatabaseConnection
import json

db = DatabaseConnection()

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        
        db.create_menu_list()
        
        


    def tearDown(self):
        clear_user = "TRUNCATE TABLE users CASCADE"
        clear_order = "TRUNCATE TABLE orders CASCADE"
        clear_menu = "TRUNCATE TABLE menu CASCADE"
        db.cursor.execute(clear_user)
        db.cursor.execute(clear_order)
        db.cursor.execute(clear_menu)
        





    # def signin(self, login):
    #     response = self.client.post('/auth/sigin', data = json.dumps(login), headers = {'Authorization': 'Bearer ' + access_token}, content_type = 'application/json')
    #     return response

if __name__ == '__main__':
    unittest.main()
