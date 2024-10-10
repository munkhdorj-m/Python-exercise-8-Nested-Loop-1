import pytest
import inspect
from assignment import print_pattern_1, print_pattern_2, print_pattern_3

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

def test1(capsys):
    expected_output = (
        "1 2 3 4 5 \n"
        "1 2 3 4 \n"
        "1 2 3 \n"
        "1 2 \n"
        "1 \n"
    )
    print_pattern_1(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test2(capsys):
    expected_output = "1 \n2 3 \n4 5 6 \n7 8 9 10 \n11 12 13 14 15 \n" 
    print_pattern_2(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test3(capsys):
    expected_output = "    *\n   **\n  ***\n ****\n*****\n"
    print_pattern_3(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output
