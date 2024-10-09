import pytest
import inspect
from assignment import print_pattern_1, print_pattern_2, print_pattern_3, print_pattern_4

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

def capsys(self, capsys):
    self.capsys = capsys

def test1(self):
    expected_output = "* * * \n" * 5 
    print_pattern_1(5)
    captured = self.capsys.readouterr()
    assert captured.out == expected_output

def test2(self):
    expected_output = "1 \n2 1 \n3 2 1 \n4 3 2 1 \n5 4 3 2 1 \n" 
    print_pattern_2(5)
    captured = self.capsys.readouterr()
    assert captured.out == expected_output

def test3(self):
    expected_output = "1 \n2 3 \n4 5 6 \n7 8 9 10 \n11 12 13 14 15 \n" 
    print_pattern_3(5)
    captured = self.capsys.readouterr()
    assert captured.out == expected_output

def test4(self):
    expected_output = "    *\n   **\n  ***\n ****\n*****\n" 
    print_pattern_4(5)
    captured = self.capsys.readouterr()
    assert captured.out == expected_output
