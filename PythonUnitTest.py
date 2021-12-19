import unittest
from calculator import calculator


class PythonUnitTest(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator()

    def test_maximum(self):
        self.assertEqual(self.calculator.maximum([1, 2, 3, 4]), 4)
        self.assertEqual(self.calculator.maximum([0, 0, 0]), 0)
        self.assertEqual(self.calculator.maximum([-1, -4, -3, -8]), -1)
        self.assertEqual(self.calculator.maximum([-100, 0, 6, 24, 100, 345]), 345)

    def test_minimum(self):
        self.assertEqual(self.calculator.minimum([1, 2, 3, 4]), 1)
        self.assertEqual(self.calculator.minimum([0, 0, 0, 0]), 0)
        self.assertEqual(self.calculator.minimum([0, 2, -2, -7]), -7)
        self.assertEqual(self.calculator.minimum([-1, -2, -3, -4]), -4)
        self.assertEqual(self.calculator.minimum([-56, 0, 64, 129]), -56)

    def test_sum_numbers(self):
        self.assertEqual(self.calculator.sum_numbers([1, 2, 3, 4]), 10)
        self.assertEqual(self.calculator.sum_numbers([0, 0, 0, 0]), 0)
        self.assertEqual(self.calculator.sum_numbers([-1, -2, -3, -4]), -10)
        self.assertEqual(self.calculator.sum_numbers([0, 29, 34, 41]), 104)

    def test_multiplication_numbers(self):
        self.assertEqual(self.calculator.multiplication_numbers([1, 2, 3, 4]), 24)
        self.assertEqual(self.calculator.multiplication_numbers([0, 0, 0, 0]), 0)
        self.assertEqual(self.calculator.multiplication_numbers([-1, -2, -3, -4]), 24)
        self.assertEqual(self.calculator.multiplication_numbers([-1, 0, 3, 54]), 0)
        self.assertEqual(self.calculator.multiplication_numbers([-1, 2, -3, -4]), -24)


if __name__ == "__main__":
    unittest.main()