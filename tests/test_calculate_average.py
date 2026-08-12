"""
Tests for the calculate_average function.
"""
import pytest
from utils.calculate_average import calculate_average

def test_calculate_average():
    numbers = [1, 2, 3, 4, 5]
    assert calculate_average(numbers) == 3.0

def test_calculate_average_empty_list():
    numbers = []
    with pytest.raises(ZeroDivisionError):
        calculate_average(numbers)

def test_calculate_average_single_element():
    numbers = [5]
    assert calculate_average(numbers) == 5.0