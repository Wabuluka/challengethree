from tests.base_test import BaseTest
order = {
    "orderId": 3,
    "userId": 1,
    "menuId": 1
}
class OrderTest(BaseTest):

    def test_get_orders(self):
        response = self.client.get('/orders')
        self.assertEqual(response.status_code, 200)

    def test_get_order(self):
        response = self.client.get('/orders/1')
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        response = self.client.post('/orders/1', json = dict(order))
        self.assertEqual(response.status_code, 200)

    # def test_update_order(self):
    #     response = self.client.put('/orders/', json = dict(order))
    #     self.assertEqual(response.status_code, 200)
