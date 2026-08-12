"""
This module provides a function to sort a list in ascending or descending order.
"""
def sort_list(input_list, order='asc'):
    """
    Sorts a list in ascending or descending order.

    Args:
        input_list (list): The list to be sorted.
        order (str, optional): The order of sorting. Defaults to 'asc'.

    Returns:
        list: The sorted list.
    """
    if order == 'asc':
        return sorted(input_list)
    elif order == 'desc':
        return sorted(input_list, reverse=True)
    else:
        raise ValueError("Invalid order. Order must be 'asc' or 'desc'.")