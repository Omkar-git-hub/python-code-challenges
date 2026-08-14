"""
Test module for calculate_multiplication function.
"""
import pytest
from utils.calculate_multiplication import calculate_multiplication

def test_calculate_multiplication():
    assert calculate_multiplication(5, 3) == 15
    assert calculate_multiplication(-5, 3) == -15
    assert calculate_multiplication(-5, -3) == 15