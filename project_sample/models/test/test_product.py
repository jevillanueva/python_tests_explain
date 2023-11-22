import unittest
from models.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.name = "iPhone"
        self.price = 500.0
        self.smartphone = Product(self.name, self.price)

    def test_product_example(self):
        self.assertEqual(2, 2) 

    def test_product_object(self):
        name = "Manzana"
        price = 1.5
        product = Product(name, price)
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)