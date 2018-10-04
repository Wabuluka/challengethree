from tests.base_test import BaseTest
from . import user

class TestUser(BaseTest):
    def test_nothing(self):
        pass

    def test_create_order(self):
        # testing the user sign in endpoint
        response = self.client.post('/api/v1/auth/signin/', json=dict(user))
        self.assertEqual(response.status_code, 200)
