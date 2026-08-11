"""
This module provides tests for the sum_of_list_elements function.
"""
import pytest
from utils.sum_of_list_elements import sum_of_list_elements

def test_sum_of_list_elements_empty_list():
    assert sum_of_list_elements([]) == 0

def test_sum_of_list_elements_single_element():
    assert sum_of_list_elements([5]) == 5

def test_sum_of_list_elements_multiple_elements():
    assert sum_of_list_elements([1, 2, 3, 4, 5]) == 15

def test_sum_of_list_elements_negative_numbers():
    assert sum_of_list_elements([-1, -2, -3, -4, -5]) == -15

def test_sum_of_list_elements_mixed_numbers():
    assert sum_of_list_elements([-1, 2, -3, 4, -5]) == -3