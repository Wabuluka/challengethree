from tests.base_test import BaseTest

class MenuTest(BaseTest):

    def test_get_menu_items(self):
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)

    # def test_get_menu_item(self):
    #     response = self.client.get('/menu/1')
    #     self.assertEqual(response.status, 200)