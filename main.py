def find_max(a, b):
    """Return the maximum of two numbers."""
    return max(a, b)

def main():
    num1 = 10
    num2 = 20
    max_num = find_max(num1, num2)
    print(f"The maximum of {num1} and {num2} is {max_num}")

if __name__ == "__main__":
    main()