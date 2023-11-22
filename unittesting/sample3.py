import unittest

class TestExample(unittest.TestCase):
    def test_suma_numeros(self):
        numero1 = 20
        numero2 = 20
        resultado = numero1 + numero2
        self.assertEqual(resultado, 40)

    def test_resta_numeros(self):
        self.assertEqual(20 - 10, 10)

if __name__ == '__main__':
    unittest.main()