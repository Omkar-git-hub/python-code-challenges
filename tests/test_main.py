import sys
import io
import unittest
from unittest.mock import patch
from main import *

class TestMain(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_name(self, mock_stdout):
        print("Your Name")
        self.assertEqual(mock_stdout.getvalue().strip(), "Your Name")