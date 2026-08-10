"""
Tests for the find_square_root function.
"""
import pytest
from utils.find_square_root import find_square_root

def test_find_square_root_positive():
    assert find_square_root(4) == 2
    assert find_square_root(9) == 3
    assert find_square_root(16) == 4

def test_find_square_root_zero():
    assert find_square_root(0) == 0

def test_find_square_root_negative():
    with pytest.raises(ValueError):
        find_square_root(-1)
    with pytest.raises(ValueError):
        find_square_root(-4)
    with pytest.raises(ValueError):
        find_square_root(-9)