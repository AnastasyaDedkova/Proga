import unittest
#import pytest

from src.lab1.calculator import *


class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, -90), -85)
        self.assertAlmostEqual(add(0.01, 0.003), 0.013)

    def test_sub(self):
        self.assertEqual(sub(6, 8), -2)
        self.assertAlmostEqual(sub(0.009, 0.003), 0.006)

    def test_mult(self):
        self.assertEqual(mult(0, 8), 0)
        self.assertAlmostEqual(mult(0.2, 3), 0.6)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(2, 10), 0.2)
        self.assertEqual(div(0.009, 0.003), 3)
        self.assertEqual(div(7, 0), "Делить на ноль нельзя")






if __name__ == '__main__':
    unittest.main()
