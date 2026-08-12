"""
This module provides tests for the find_second_largest function.
"""
import unittest
from utils.find_second_largest import find_second_largest

class TestFindSecondLargest(unittest.TestCase):
    def test_find_second_largest(self):
        self.assertEqual(find_second_largest([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_second_largest([5, 5, 5, 5]), None)
        self.assertEqual(find_second_largest([1, 1, 2, 2, 3]), 2)
        self.assertEqual(find_second_largest([]), None)
        self.assertEqual(find_second_largest([1]), None)