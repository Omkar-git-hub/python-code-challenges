"""
Module to check if a number is positive or negative.
"""
def check_positive_negative(num: int) -> str:
    """
    Checks if a number is positive or negative.

    Args:
        num (int): The number to check.

    Returns:
        str: "Positive" if the number is positive, "Negative" if the number is negative, "Zero" if the number is zero.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"