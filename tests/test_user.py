from tests.base_test import BaseTest
from . import user, new_user, user_in

class TestUser(BaseTest):
    # def test_nothing(self):
    #     pass

    def test_create_user(self):
        # testing the user sign in endpoint
        response = self.client.post('/api/v1/auth/singup', json=dict(user))
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 201)
    
    def test_signin_user(self):
        #testing for user siginin endpoint
        response = self.client.post('/api/v1/auth/signin', json=dict(user_in))
        self.assertEqual(response.status_code, 200)

    def test_user_orders(self):
        #testing for user siginin endpoint
        response = self.client.post('/api/v1/users/orders', json=dict(user_in))
        self.assertEqual(response.status_code, 200)
