from main import subtract_two_numbers

def test_subtract_two_numbers():
    assert subtract_two_numbers(5, 3) == 2
    assert subtract_two_numbers(-5, 3) == -8
    assert subtract_two_numbers(-5, -3) == -2