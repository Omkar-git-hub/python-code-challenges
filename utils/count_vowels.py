"""
Module to count vowels in a given string.

This module provides a function to count the number of vowels in a string.
"""
def count_vowels(input_string: str) -> int:
    """
    Count the number of vowels in a given string.

    Args:
        input_string (str): The input string to count vowels from.

    Returns:
        int: The number of vowels in the input string.
    """
    vowels = 'aeiou'
    return sum(1 for char in input_string.lower() if char in vowels)