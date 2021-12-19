import unittest
from Sources.calculator import calculator


class PythonUnitTest(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator()

    def test_maximum(self):
        self.assertEqual(self.calculator.maximum([1, 2, 3, 4]), 4)

    def test_minimum(self):
        self.assertEqual(self.calculator.minimum([1, 2, 3, 4]), 1)

    def test_sum_numbers(self):
        self.assertEqual(self.calculator.sum_numbers([1, 2, 3, 4]), 10)

    def test_multiplication_numbers(self):
        self.assertEqual(self.calculator.multiplication_numbers([1, 2, 3, 4]), 24)
