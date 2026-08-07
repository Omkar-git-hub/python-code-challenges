from main import multiply_two_numbers

def test_multiply_two_numbers():
    assert multiply_two_numbers(2, 3) == 6
    assert multiply_two_numbers(-2, 3) == -6
    assert multiply_two_numbers(0, 3) == 0