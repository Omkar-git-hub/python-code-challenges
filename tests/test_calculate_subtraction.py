"""
Test module for calculate_subtraction function.
"""
import pytest
from utils.calculate_subtraction import calculate_subtraction

def test_calculate_subtraction():
    assert calculate_subtraction(5, 3) == 2
    assert calculate_subtraction(-5, 3) == -8
    assert calculate_subtraction(-5, -3) == -2