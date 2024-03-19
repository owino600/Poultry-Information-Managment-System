#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.inventory import Inventory
from models.sales import Sales

class TestSales(unittest.TestCase):
    def setUp(self):
        self.sale = Sales(Product_id=1, Product_name='Chicken', Category=101, Description='Farm raised chicken', quantity=5, unit_price=20.0, supplier='Local Farm', date_received=datetime.utcnow(), Expiration_date=datetime.utcnow())

    def test_attributes(self):
        self.assertEqual(self.sale.Product_id, 1)
        self.assertEqual(self.sale.Product_name, 'Chicken')
        self.assertEqual(self.sale.Category, 101)
        self.assertEqual(self.sale.Description, 'Farm raised chicken')
        self.assertEqual(self.sale.quantity, 5)
        self.assertEqual(self.sale.unit_price, 20.0)
        self.assertEqual(self.sale.supplier, 'Local Farm')

if __name__ == '__main__':
    unittest.main()