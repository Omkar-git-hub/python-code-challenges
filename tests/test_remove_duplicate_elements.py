"""
Tests for the remove_duplicate_elements function.
"""
import unittest
from utils.remove_duplicate_elements import remove_duplicate_elements

class TestRemoveDuplicateElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicate_elements([]), [])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicate_elements([1, 2, 3]), [1, 2, 3])

    def test_with_duplicates(self):
        self.assertEqual(set(remove_duplicate_elements([1, 2, 2, 3, 3, 3])), {1, 2, 3})

    def test_with_negative_numbers(self):
        self.assertEqual(set(remove_duplicate_elements([-1, -2, -2, -3, -3, -3])), {-1, -2, -3})

    def test_with_strings(self):
        self.assertEqual(set(remove_duplicate_elements(['a', 'b', 'b', 'c', 'c', 'c'])), {'a', 'b', 'c'})