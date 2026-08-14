"""
Tests for the count_words module.
"""
import pytest
from utils.count_words import count_words_in_file

def test_count_words_in_file(tmp_path):
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w') as file:
        file.write("This is a test file.")
    assert count_words_in_file(file_path) == 5

def test_count_words_in_file_empty(tmp_path):
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w') as file:
        file.write("")
    assert count_words_in_file(file_path) == 0

def test_count_words_in_file_not_found():
    assert count_words_in_file("non_existent_file.txt") is None