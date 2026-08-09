"""
This module provides a function to calculate the square root of a number.
"""
import math

def find_square_root(number):
    """
    Calculate the square root of a number.

    Args:
        number (float): The number to find the square root of.

    Returns:
        float: The square root of the number.

    Raises:
        ValueError: If the number is negative.
    """
    if number < 0:
        raise ValueError("Cannot find square root of a negative number")
    return math.sqrt(number)