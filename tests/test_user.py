from tests.base_test import BaseTest

new_user = {
    'userId': 4,
    'username': 'josh',
    'password': '123'
}
class UserTest(BaseTest):
    
    def test_create_user(self):
        response = self.client.post('api/v1/auth/signup', json=dict(new_user))
        self.assertEqual(response.status_code, 200)
