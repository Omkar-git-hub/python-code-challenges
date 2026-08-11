"""
Test module for count_vowels function.
"""
import unittest
from utils.count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfgh"), 0)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_mixed_string(self):
        self.assertEqual(count_vowels("hello world"), 3)

    def test_case_insensitivity(self):
        self.assertEqual(count_vowels("Hello World"), 3)

if __name__ == '__main__':
    unittest.main()