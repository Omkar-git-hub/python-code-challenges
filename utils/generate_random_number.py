"""
Module to generate a random number.
"""
import random

def generate_random_number(min_value: int = 0, max_value: int = 100) -> int:
    """
    Generate a random integer within a specified range.

    Args:
    min_value (int): The minimum value for the random number (inclusive). Defaults to 0.
    max_value (int): The maximum value for the random number (inclusive). Defaults to 100.

    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)