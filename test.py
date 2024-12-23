import unittest
from main import add, subtract, multiply, divide, calculate_remainder

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(5, 0), 5)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(3, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 3), 0.6666666666666666)
        self.assertEqual(divide(-1, 1), -1)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)

    def test_calculate_remainder(self):
        self.assertEqual(calculate_remainder(12, 3), 0)
        self.assertEqual(calculate_remainder(8, 4), 0)
        self.assertEqual(calculate_remainder(10, 4), 2)

        with self.assertRaises(ZeroDivisionError):
            calculate_remainder(10, 0)

if __name__ == '__main__':
    unittest.main()
