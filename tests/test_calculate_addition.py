"""
Test module for calculate_addition function.
"""
import pytest
from utils.calculate_addition import calculate_addition

def test_calculate_addition():
    assert calculate_addition(5, 3) == 8
    assert calculate_addition(-5, 3) == -2
    assert calculate_addition(-5, -3) == -8