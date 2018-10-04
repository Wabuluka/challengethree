import unittest
from app import app
from app.models.database import DatabaseConnection
import json


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        db = DatabaseConnection()
        db.create_menu_list()
        
        


    def tearDown(self):
        # clear_user = "DELETE FROM users CASCADE"
        # db = DatabaseConnection()
        # cur.database()
        # db.drop_data_from_orders_table()
        # cur.execute(clear_user)
        pass
    





    # def signin(self, login):
    #     response = self.client.post('/auth/sigin', data = json.dumps(login), headers = {'Authorization': 'Bearer ' + access_token}, content_type = 'application/json')
    #     return response

if __name__ == '__main__':
    unittest.main()