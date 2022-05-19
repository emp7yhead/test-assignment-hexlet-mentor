"""Tests for fizzbuzz."""
import pytest
from fizzbuzz.fizzbuzz_calculator import get_fizz_buzz


def test_fizz():
    """Tests for Fizz result."""
    assert get_fizz_buzz(81) == 'Fizz'


def test_buzz():
    """Tests for Buzz result."""
    assert get_fizz_buzz(100) == 'Buzz'


def test_get_fizz_buzz():
    """Test for FizzBuzz result."""
    assert get_fizz_buzz(45) == 'FizzBuzz'


def test_number():
    """Test for number result."""
    assert get_fizz_buzz(2) == 2


def test_edge_cases():
    """Test for edge cases."""
    assert get_fizz_buzz(0) == 'FizzBuzz'
    assert get_fizz_buzz(-1) == -1
    assert get_fizz_buzz(3 * 5) == 'FizzBuzz'


@pytest.mark.xfail
def test_error():
    """Test for error."""
    assert get_fizz_buzz(0.1)