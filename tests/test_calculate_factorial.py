"""
Test module for the calculate_factorial function.

This module provides test cases for the calculate_factorial function.
The test cases cover different scenarios, including positive numbers, zero, and negative numbers.

Author: [Your Name]
Date: [Today's Date]
"""

import pytest
from utils.calculate_factorial import calculate_factorial

def test_calculate_factorial_positive():
    assert calculate_factorial(5) == 120

def test_calculate_factorial_zero():
    assert calculate_factorial(0) == 1

def test_calculate_factorial_one():
    assert calculate_factorial(1) == 1

def test_calculate_factorial_negative():
    with pytest.raises(ValueError):
        calculate_factorial(-1)