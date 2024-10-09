import pytest
import inspect
from assignment import find_highest_digit, repeat_number, is_prime_number

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("num, expected", [
    (1234, 4),
    (91635, 9),
    (0, 0),
])
def test1(num, expected):
    assert find_highest_digit(num) == expected
    assert check_contains_loop(find_highest_digit)

@pytest.mark.parametrize("num, expected", [
    (4, 4444),
    (7, 7777777),
    (1, 1),
])
def test2(num, expected):
    assert repeat_number(num) == expected
    assert check_contains_loop(repeat_number)

@pytest.mark.parametrize("num, expected", [
    (3, True),
    (18, False),
    (41, True),
    (1, False)
])
def test3(num, expected):
    assert is_prime_number(num) == expected
    assert check_contains_loop(is_prime_number)
