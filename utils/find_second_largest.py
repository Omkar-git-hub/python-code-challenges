"""
This module provides a function to find the second largest number in a list of numbers.
"""
def find_second_largest(numbers):
    """
    Find the second largest number in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The second largest number in the list. If the list has less than two unique elements, returns None.
    """
    if len(set(numbers)) < 2:
        return None
    return sorted(set(numbers), reverse=True)[1]