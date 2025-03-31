import pytest
from main import add_numbers

def test_add_numbers():
    # Test with a list of positive integers
    assert add_numbers([1, 2, 3, 4]) == 10

    # Test with a list of mixed positive and negative integers
    assert add_numbers([1, -2, 3, -4]) == -2

    # Test with an empty list
    assert add_numbers([]) == 0

    # Test with a list containing zeroes
    assert add_numbers([0, 0, 0]) == 0

    # Test with a single number
    assert add_numbers([10]) == 10

    # Test with large numbers
    assert add_numbers([1000000, 5000000, 2000000]) == 8000000

    # Failed test case
    assert add_numbers([10, 20, 30]) == 59
