"""Logic for FizzBuzz."""

from typing import Union

FIZZ_DIVIDER = 3
BUZZ_DIVIDER = 5


def get_fizz_buzz(number: int) -> Union[str, int]:
    """Check number for fizzbuzz.

    Args:
        number: puzzled number.

    Returns:
        str: result string.
    """
    final_result = ''
    if number % FIZZ_DIVIDER == 0:
        final_result += 'Fizz'
    if number % BUZZ_DIVIDER == 0:
        final_result += 'Buzz'
    return final_result if final_result else number
