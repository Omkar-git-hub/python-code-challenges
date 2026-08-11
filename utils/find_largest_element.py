"""
This module contains a function to find the largest element in a list.
"""
def find_largest_element(lst):
    """
    Find the largest element in a list.

    Args:
        lst (list): A list of elements.

    Returns:
        The largest element in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)