"""
Tests for the check_palindrome function.
"""
import pytest
from utils.check_palindrome import check_palindrome

def test_check_palindrome():
    assert check_palindrome("radar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("A man, a plan, a canal: Panama") == True
    assert check_palindrome("Not a palindrome") == False

def test_check_palindrome_empty_string():
    assert check_palindrome("") == True

def test_check_palindrome_single_character():
    assert check_palindrome("a") == True