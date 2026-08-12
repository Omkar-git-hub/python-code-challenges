"""
This module provides tests for the sort_list function.
"""
import pytest
from utils.sort_list import sort_list

def test_sort_list_asc():
    input_list = [5, 2, 8, 1, 9]
    expected_output = [1, 2, 5, 8, 9]
    assert sort_list(input_list) == expected_output

def test_sort_list_desc():
    input_list = [5, 2, 8, 1, 9]
    expected_output = [9, 8, 5, 2, 1]
    assert sort_list(input_list, order='desc') == expected_output

def test_sort_list_invalid_order():
    input_list = [5, 2, 8, 1, 9]
    with pytest.raises(ValueError):
        sort_list(input_list, order='invalid')