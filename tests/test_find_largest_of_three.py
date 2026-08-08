"""
Tests for the find_largest_of_three function.
"""
import unittest
from utils.find_largest_of_three import find_largest

class TestFindLargestOfThree(unittest.TestCase):
    def test_largest_first(self):
        self.assertEqual(find_largest(5, 3, 1), 5)

    def test_largest_second(self):
        self.assertEqual(find_largest(1, 5, 3), 5)

    def test_largest_third(self):
        self.assertEqual(find_largest(1, 3, 5), 5)

    def test_equal_numbers(self):
        self.assertEqual(find_largest(5, 5, 5), 5)