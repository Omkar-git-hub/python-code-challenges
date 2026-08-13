"""
Module to read a text file.

This module provides a function to read the contents of a text file.
"""

def read_text_file(file_path):
    """
    Reads the contents of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The contents of the text file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None