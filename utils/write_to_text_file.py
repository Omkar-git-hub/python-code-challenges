"""
Module to write to a text file.

This module provides a function to write a given text to a file.
"""

def write_to_file(filename, text):
    """
    Write the given text to the specified file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
    """
    with open(filename, 'w') as file:
        file.write(text)