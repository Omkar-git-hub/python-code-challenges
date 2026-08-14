"""
Test module for calculate_division function.
"""
import pytest
from utils.calculate_division import calculate_division

def test_calculate_division():
    assert calculate_division(5, 3) == 5/3
    assert calculate_division(-5, 3) == -5/3
    assert calculate_division(-5, -3) == 5/3

    with pytest.raises(ZeroDivisionError):
        calculate_division(5, 0)