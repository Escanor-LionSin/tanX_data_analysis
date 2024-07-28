import unittest
from script import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, get_top_customers

class TestRevenueCalculations(unittest.TestCase):
    def setUp(self):
        self.sample_orders = [
            {'order_date': '2023-01-15', 'product_price': '10', 'quantity': '2', 'product_id': 'P1', 'customer_id': 'C1'},
            {'order_date': '2023-01-20', 'product_price': '15', 'quantity': '1', 'product_id': 'P2', 'customer_id': 'C2'},
            {'order_date': '2023-02-05', 'product_price': '20', 'quantity': '3', 'product_id': 'P1', 'customer_id': 'C1'},
        ]

    def test_compute_monthly_revenue(self):
        expected = {'2023-01': 35.0, '2023-02': 60.0}
        self.assertEqual(compute_monthly_revenue(self.sample_orders), expected)

    def test_compute_product_revenue(self):
        expected = {'P1': 80.0, 'P2': 15.0}
        self.assertEqual(compute_product_revenue(self.sample_orders), expected)

    def test_compute_customer_revenue(self):
        expected = {'C1': 80.0, 'C2': 15.0}
        self.assertEqual(compute_customer_revenue(self.sample_orders), expected)

    def test_get_top_customers(self):
        customer_revenue = {'C1': 80.0, 'C2': 15.0, 'C3': 50.0}
        expected = [('C1', 80.0), ('C3', 50.0), ('C2', 15.0)]
        self.assertEqual(get_top_customers(customer_revenue), expected)

if __name__ == '__main__':
    unittest.main()