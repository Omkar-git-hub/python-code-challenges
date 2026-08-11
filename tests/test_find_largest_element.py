"""
This module contains tests for the find_largest_element function.
"""
import unittest
from utils.find_largest_element import find_largest_element

class TestFindLargestElement(unittest.TestCase):
    def test_find_largest_element(self):
        self.assertEqual(find_largest_element([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_largest_element([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(find_largest_element([10, 20, 30, 40, 50]), 50)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_largest_element([])

    def test_single_element_list(self):
        self.assertEqual(find_largest_element([5]), 5)

    def test_duplicate_elements(self):
        self.assertEqual(find_largest_element([1, 2, 2, 3, 3, 3]), 3)