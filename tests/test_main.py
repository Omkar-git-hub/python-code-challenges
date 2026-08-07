import unittest
from main import find_max

class TestFindMax(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(10, 20), 20)
        self.assertEqual(find_max(20, 10), 20)
        self.assertEqual(find_max(10, 10), 10)

    def test_negative_numbers(self):
        self.assertEqual(find_max(-10, 20), 20)
        self.assertEqual(find_max(10, -20), 10)
        self.assertEqual(find_max(-10, -20), -10)

if __name__ == "__main__":
    unittest.main()