"""
Module to check if a number is prime.

This module provides a function to determine whether a given number is prime.
"""
def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True