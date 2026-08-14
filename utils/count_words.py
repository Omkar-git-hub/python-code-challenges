"""
Module to count words in a text file.
"""
import re

def count_words_in_file(file_path):
    """
    Count the number of words in a text file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        int: Number of words in the file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
            return len(words)
    except FileNotFoundError:
        return None