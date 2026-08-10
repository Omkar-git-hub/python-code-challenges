"""
Module to check if a given string is a palindrome.

A palindrome is a string that reads the same backwards as forwards.
"""
def check_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]