from tests.base_test import BaseTest
from . import user, new_user

class TestUser(BaseTest):
    def test_nothing(self):
        pass

    def test_create_order(self):
        # testing the user sign in endpoint
        response = self.client.post('/api/v1/auth/signin/1', json=dict(user))
        self.assertEqual(response.status_code, 200)


class UserTest(BaseTest):
    
    def test_create_user(self):
        response = self.client.post('api/v1/auth/signup', json=dict(new_user))
        self.assertEqual(response.status_code, 200)
