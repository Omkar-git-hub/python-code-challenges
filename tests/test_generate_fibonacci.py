"""
Tests for the generate_fibonacci function.
"""
import unittest
from utils.generate_fibonacci import generate_fibonacci

class TestGenerateFibonacci(unittest.TestCase):
    def test_generate_fibonacci_zero(self):
        self.assertEqual(generate_fibonacci(0), [])

    def test_generate_fibonacci_one(self):
        self.assertEqual(generate_fibonacci(1), [0])

    def test_generate_fibonacci_two(self):
        self.assertEqual(generate_fibonacci(2), [0, 1])

    def test_generate_fibonacci_more(self):
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3])

    def test_generate_fibonacci_large(self):
        self.assertEqual(generate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])