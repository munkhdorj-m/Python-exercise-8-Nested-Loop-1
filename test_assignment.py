import pytest
import inspect
from assignment import print_pattern_1, print_pattern_2, print_pattern_3, print_pattern_4

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("n, expected_output", [
    (5, "\n".join(["* " * 5] * 5)),
    (3, "\n".join(["* " * 3] * 3)),
])
def test1(n, expected_output, capsys):
    print_pattern_1(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()
    assert check_contains_loop(print_pattern_1)

@pytest.mark.parametrize("n, expected_output", [
    (5, "\n".join([" ".join(str(j) for j in range(1, i + 1)) for i in range(n, 0, -1)])),
    (3, "\n".join([" ".join(str(j) for j in range(1, i + 1)) for i in range(3, 0, -1)])),
])
def test2(n, expected_output, capsys):
    print_pattern_2(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()
    assert check_contains_loop(print_pattern_1)

@pytest.mark.parametrize("n, expected_output", [
    (5, "\n".join([" ".join(str(count + j) for j in range(i)) for i in range(1, 6) for count in [sum(range(i))]])),
    (3, "\n".join([" ".join(str(count + j) for j in range(i)) for i in range(1, 4) for count in [sum(range(i))]])),
])
def test3(n, expected_output, capsys):
    print_pattern_3(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()
    assert check_contains_loop(print_pattern_1)

@pytest.mark.parametrize("n, expected_output", [
    (5, "\n".join([" " * (n - i) + "*" * i for i in range(1, 6)])),
    (3, "\n".join([" " * (n - i) + "*" * i for i in range(1, 4)])),
])
def test4(n, expected_output, capsys):
    print_pattern_4(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()
    assert check_contains_loop(print_pattern_1)
