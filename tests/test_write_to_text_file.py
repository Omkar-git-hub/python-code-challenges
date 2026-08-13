"""
Tests for the write_to_text_file module.
"""

import unittest
from utils.write_to_text_file import write_to_file
import os

class TestWriteToTextFile(unittest.TestCase):
    def test_write_to_file(self):
        filename = 'test.txt'
        text = 'Hello, World!'
        write_to_file(filename, text)
        with open(filename, 'r') as file:
            self.assertEqual(file.read(), text)
        os.remove(filename)

    def test_write_to_file_empty(self):
        filename = 'test.txt'
        text = ''
        write_to_file(filename, text)
        with open(filename, 'r') as file:
            self.assertEqual(file.read(), text)
        os.remove(filename)

    def test_write_to_file_none(self):
        filename = 'test.txt'
        text = None
        with self.assertRaises(TypeError):
            write_to_file(filename, text)