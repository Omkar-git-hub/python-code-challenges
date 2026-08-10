"""
Tests for the check_even_odd function.
"""
import unittest
from utils.check_even_odd import check_even_odd

class TestCheckEvenOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(check_even_odd(4), "Even")

    def test_odd(self):
        self.assertEqual(check_even_odd(3), "Odd")

    def test_zero(self):
        self.assertEqual(check_even_odd(0), "Even")

    def test_negative(self):
        self.assertEqual(check_even_odd(-4), "Even")
        self.assertEqual(check_even_odd(-3), "Odd")