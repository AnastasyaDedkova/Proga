import unittest

from src.lab2.rsa import *

class RSATestCase(unittest.TestCase):  # тест корректной работы фунции проверки числа на простоту
    def test_is_prime(self):
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(1000), False)
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)

    def test_gcd(self): # тест корректной работы фунции нахождения наибольшего общего делителя
        self.assertEqual(gcd(10, 25), 5)
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(11, 13), 1)

    def test_multiplicative_inverse(self): # тест корректной работы фунции нахождения обратного множителя
        self.assertEqual(multiplicative_inverse(2, 10), -1)
        self.assertEqual(multiplicative_inverse(2, 20), -1)
        self.assertEqual(multiplicative_inverse(2, 25), 13)



if __name__ == '__main__':
    unittest.main()
