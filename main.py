def swap_variables(a, b):
    """
    Swap two variables.

    Args:
        a (any): The first variable.
        b (any): The second variable.

    Returns:
        tuple: A tuple containing the swapped variables.
    """
    return b, a

def main():
    var1 = 5
    var2 = 10
    print("Before swap: var1 =", var1, ", var2 =", var2)
    var1, var2 = swap_variables(var1, var2)
    print("After swap: var1 =", var1, ", var2 =", var2)

if __name__ == "__main__":
    main()