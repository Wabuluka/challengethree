from tests.base_test import BaseTest
from .import order
class OrderTest(BaseTest):
    def test_nothing(self):
        pass
        
    # def test_get_orders(self):
    #     response = self.client.get('/orders')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_order(self):
    #     response = self.client.get('/orders/1')
    #     self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        response = self.client.post(
            '/api/v1/orders/1', json=dict(order))
        self.assertEqual(response.status_code, 200)

    # def test_update_order(self):
    #     response = self.client.put('/orders/', json = dict(order))
    #     self.assertEqual(response.status_code, 200)
