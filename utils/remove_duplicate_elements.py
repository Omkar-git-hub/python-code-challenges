"""
This module provides a function to remove duplicate elements from a list.
"""
def remove_duplicate_elements(input_list):
    """
    Removes duplicate elements from a list.

    Args:
        input_list (list): The list from which to remove duplicates.

    Returns:
        list: A new list with duplicate elements removed.
    """
    return list(set(input_list))