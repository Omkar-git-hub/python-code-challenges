from main import swap_variables, add, subtract, multiply, divide

def test_swap_variables():
    assert swap_variables(1, 2) == (2, 1)

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(4, 2) == 2

    try:
        divide(4, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError as e:
        assert str(e) == "Cannot divide by zero"