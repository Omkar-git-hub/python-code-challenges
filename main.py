"""
This module contains the main function to subtract two numbers.
"""
def subtract_two_numbers(a, b):
    """
    This function subtracts two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The result of subtracting b from a.
    """
    return a - b

def main():
    # Example usage:
    result = subtract_two_numbers(10, 5)
    print("Result:", result)

if __name__ == "__main__":
    main()