"""
Module to calculate the quotient of two numbers.
"""
def calculate_division(num1, num2):
    """
    Calculate the quotient of two numbers.

    Args:
        num1 (int): The dividend.
        num2 (int): The divisor.

    Returns:
        float: The quotient of num1 and num2.

    Raises:
        ZeroDivisionError: If num2 is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2