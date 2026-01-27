import unittest
from pytest import approx
from src.Calculator import add, subtract, multiply, divide  # avoid import *

class SumTest(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(4, 5), 9)

    def test_negative(self):
        self.assertEqual(add(-4, 5), 1)

    def test_decimal(self):
        self.assertEqual(add(2.06, 3.18), 5.24)

class SubtractTest(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(subtract(4, 5), -1)

    def test_negative(self):
        self.assertEqual(subtract(-4, 5), -9)

class MultiplyTest(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_negative(self):
        self.assertEqual(multiply(-4, 5), -20)

class DivideTest(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(divide(10, 5), 2)

    def test_negative(self):
        self.assertEqual(divide(-10, 5), -2)

    def test_decimal(self):
        self.assertEqual(divide(8.68, 3.11), approx(2.79, 1e-3))

if __name__ == "__main__":
    unittest.main()
