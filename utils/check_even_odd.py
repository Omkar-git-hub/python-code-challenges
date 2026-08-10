"""
This module provides a function to check if a number is even or odd.
"""
def check_even_odd(num: int) -> str:
    """
    Checks if a number is even or odd.

    Args:
        num (int): The number to check.

    Returns:
        str: "Even" if the number is even, "Odd" otherwise.
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"