#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.sales import Sales

class TestSales(unittest.TestCase):
    def setUp(self):
        self.sale = Sales(Sales_id=1, buyer_name='John Doe', poultry_id=101, quantity_sold=5, unit_price=20.0, total_price=100.0, payment_method='Cash')

    def test_attributes(self):
        self.assertEqual(self.sale.Sales_id, 1)
        self.assertEqual(self.sale.buyer_name, 'John Doe')
        self.assertEqual(self.sale.poultry_id, 101)
        self.assertEqual(self.sale.quantity_sold, 5)
        self.assertEqual(self.sale.unit_price, 20.0)
        self.assertEqual(self.sale.total_price, 100.0)
        self.assertEqual(self.sale.payment_method, 'Cash')

    def test_calculate_total_revenue(self):
        unit_price = 20.0
        quantity_sold = 5 
        self.assertEqual(self.sale.calculate_total_revenue(unit_price, quantity_sold), 100.0)

if __name__ == '__main__':
    unittest.main()