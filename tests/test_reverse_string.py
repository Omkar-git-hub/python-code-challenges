"""
Tests for the reverse_string function.
"""
import pytest
from utils.reverse_string import reverse_string

def test_reverse_string():
    """
    Test case for reversing a string.
    """
    input_str = "Hello World"
    expected_output = "dlroW olleH"
    assert reverse_string(input_str) == expected_output

def test_reverse_string_empty():
    """
    Test case for reversing an empty string.
    """
    input_str = ""
    expected_output = ""
    assert reverse_string(input_str) == expected_output

def test_reverse_string_single_char():
    """
    Test case for reversing a single character string.
    """
    input_str = "a"
    expected_output = "a"
    assert reverse_string(input_str) == expected_output