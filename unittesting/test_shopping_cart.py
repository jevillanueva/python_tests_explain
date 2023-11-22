import unittest
from product import Product, ProductDiscountError
from shopping_cart import ShoppingCart

def is_available_to_skip():
    return True

def service_is_connected():
    return False

class TestShoppingCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass, se ejecuta antes de todos los tests")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass, se ejecuta después de todos los tests")

    def setUp(self):
        print("Se ejecuta antes de cada test")
        self.name = "iPhone"
        self.price = 500.0
        self.smartphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()

        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

    def tearDown(self):
        print("Se ejecuta después de cada test")

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


    #asserttrue y assertfalse
    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), "El carrito no está vacío")

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products(), "El carrito está vacío")
        self.assertFalse(self.shopping_cart_2.empty(), "El carrito está vacío")

    #assertin y assertnotin
    def test_product_in_shopping_cart(self):
        product = Product("Teclado", 50.0)
        self.shopping_cart_2.add_product(product)
        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    #assertraises
    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name="Teclado", price=50.0, discount=51.0)

    # assertGreater, assertLess, assertEqual
    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name="Libro", price=15.0))
        self.shopping_cart_1.add_product(Product(name="Cámara", price=700.0, discount=70.0))
        self.assertGreater(self.shopping_cart_1.total, 0) # >
        self.assertLess(self.shopping_cart_1.total, 1000) # <
        self.assertEqual(self.shopping_cart_1.total, 645) # ==
        #assertGreaterEqual y assertLessEqual tambien existen

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0.0)

    #Skip Assertions
    @unittest.skip("Colocar el motivo del skip")
    def test_skip_example(self):
        self.assertEqual(1,1)

    # skipIf y skipUnless
    @unittest.skipIf(is_available_to_skip(), "Skip saltado si se cumple la condición")
    def test_skip_example_two(self):
        self.assertEqual(1,1)

    @unittest.skipUnless(service_is_connected(), "Skip saltado si no se cumple la condición")
    def test_skip_example_three(self):
        self.assertEqual(1,1)

    #assertRegex
    def test_code_product(self):
        self.assertRegex(self.smartphone.code, self.smartphone.name)
if __name__ == '__main__':
    unittest.main()