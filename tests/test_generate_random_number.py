"""
Tests for the generate_random_number function.
"""
import unittest
from utils.generate_random_number import generate_random_number

class TestGenerateRandomNumber(unittest.TestCase):
    def test_default_range(self):
        random_number = generate_random_number()
        self.assertGreaterEqual(random_number, 0)
        self.assertLessEqual(random_number, 100)

    def test_custom_range(self):
        min_value = 10
        max_value = 20
        random_number = generate_random_number(min_value, max_value)
        self.assertGreaterEqual(random_number, min_value)
        self.assertLessEqual(random_number, max_value)

if __name__ == '__main__':
    unittest.main()