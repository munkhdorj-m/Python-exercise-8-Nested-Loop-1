import pytest
import inspect
from assignment import print_pattern_1, print_pattern_2, print_pattern_3, print_pattern_4

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("n, expected_output", [
    (5, "* * * * *\n* * * * *\n* * * * *\n* * * * *\n* * * * *"),
    (3, "* * *\n* * *\n* * *"),
])
def test1(n, expected_output, capsys):
    print_pattern_1(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
    assert check_contains_loop(print_pattern_1)

@pytest.mark.parametrize("n, expected_output", [
    (5, "1 2 3 4 5\n1 2 3 4\n1 2 3\n1 2\n1"),
    (3, "1 2 3\n1 2\n1"),
])
def test2(n, expected_output, capsys):
    print_pattern_2(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
    assert check_contains_loop(print_pattern_2)

@pytest.mark.parametrize("n, expected_output", [
    (5, "1\n2 3\n4 5 6\n7 8 9 10\n11 12 13 14 15"),
    (3, "1\n2 3\n4 5 6"),
])
def test3(n, expected_output, capsys):
    print_pattern_3(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
    assert check_contains_loop(print_pattern_3)

@pytest.mark.parametrize("n, expected_output", [
    (5, "    *\n   **\n  ***\n ****\n*****"),
    (3, "  *\n **\n***"),
])
def test4(n, expected_output, capsys):
    print_pattern_4(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
    assert check_contains_loop(print_pattern_4)
