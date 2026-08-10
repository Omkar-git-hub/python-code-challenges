"""
Module to calculate the factorial of a given number.

This module provides a function to calculate the factorial of a given integer.
The function uses recursion to calculate the factorial.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.

    Raises:
        ValueError: If the input number is negative.
    """
    if n < 0:
        raise ValueError("Input number must be non-negative.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)