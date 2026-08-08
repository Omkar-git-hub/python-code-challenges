"""
Tests for the check_positive_negative function.
"""
import pytest
from utils.check_positive_negative import check_positive_negative

def test_check_positive():
    assert check_positive_negative(5) == "Positive"

def test_check_negative():
    assert check_positive_negative(-5) == "Negative"

def test_check_zero():
    assert check_positive_negative(0) == "Zero"