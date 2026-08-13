"""
Tests for the read_text_file module.
"""

import unittest
from unittest.mock import patch
from utils.read_text_file import read_text_file
import tempfile
import os

class TestReadTextFile(unittest.TestCase):
    def test_read_text_file(self):
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
            tmp.write('Hello World!')
            file_path = tmp.name

        # Read the file
        contents = read_text_file(file_path)

        # Check the contents
        self.assertEqual(contents, 'Hello World!')

        # Remove the temporary file
        os.remove(file_path)

    def test_read_non_existent_file(self):
        # Try to read a non-existent file
        contents = read_text_file('non_existent_file.txt')

        # Check the result
        self.assertIsNone(contents)

    @patch('builtins.open', side_effect=FileNotFoundError())
    def test_read_file_with_error(self, mock_open):
        # Try to read a file with an error
        contents = read_text_file('file_with_error.txt')

        # Check the result
        self.assertIsNone(contents)