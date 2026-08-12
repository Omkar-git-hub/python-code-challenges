"""
Module to calculate the average of a list of numbers.
"""
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the list of numbers.
    """
    return sum(numbers) / len(numbers)