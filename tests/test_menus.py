from tests.base_test import BaseTest
from . import menu
class MenuTest(BaseTest):

    def test_nothing(self):
        pass

    def test_get_menu_items(self):
        response = self.client.get('/api/v1/menu')
        self.assertEqual(response.status_code, 200)

    def test_get_menu_item(self):
        response = self.client.get('/api/v1/menu/1')
        self.assertEqual(response.status, 200)

    def test_create_order(self):
        response = self.client.post('/api/v1/menu/1', json=dict(menu))
        self.assertEqual(response.status_code, 200)
