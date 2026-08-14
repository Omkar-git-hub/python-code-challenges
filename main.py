def swap_variables(a, b):
    """Swap two variables."""
    return b, a

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def check_even_odd(n):
    """Check if a number is even or odd."""
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def check_positive_negative(n):
    """Check if a number is positive or negative."""
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def check_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

def count_words(s):
    """Count the number of words in a string."""
    return len(s.split())

def find_largest_element(numbers):
    """Find the largest element in a list of numbers."""
    return max(numbers)

def find_largest_of_three(a, b, c):
    """Find the largest of three numbers."""
    return max(a, b, c)

def find_second_largest(numbers):
    """Find the second largest element in a list of numbers."""
    numbers = sorted(set(numbers))
    if len(numbers) < 2:
        return None
    return numbers[-2]

def find_square_root(n):
    """Find the square root of a number."""
    return n**0.5

def generate_fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def generate_random_number(min_val, max_val):
    """Generate a random number between min_val and max_val."""
    import random
    return random.randint(min_val, max_val)

def read_text_file(filename):
    """Read the contents of a text file."""
    with open(filename, 'r') as file:
        return file.read()

def remove_duplicate_elements(numbers):
    """Remove duplicate elements from a list of numbers."""
    return list(set(numbers))

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def sort_list(numbers):
    """Sort a list of numbers."""
    return sorted(numbers)

def sum_of_list_elements(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def write_to_text_file(filename, content):
    """Write content to a text file."""
    with open(filename, 'w') as file:
        file.write(content)

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b