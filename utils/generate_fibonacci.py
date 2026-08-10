"""
Module to generate Fibonacci series.
"""
def generate_fibonacci(n):
    """
    Generate Fibonacci series up to the nth number.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence