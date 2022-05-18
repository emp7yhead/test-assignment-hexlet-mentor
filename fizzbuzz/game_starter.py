"""Game starter for FizzBuzz."""
import sys
from typing import Callable, Union

import prompt


def start_game(game: Callable[[int], Union[str, int]]) -> None:
    """Start a game.

    Args:
        game: function that will be sented in infinite loop.
    """
    print('Welcome to Fizz Buzz!')
    print('Submit a number and get an answer!')
    while True:
        puzzled_number = prompt.string('Number: ')
        try:
            final_result = game(int(puzzled_number))
        except ValueError:
            sys.exit('Please enter an integer!')
        if isinstance(final_result, str):
            print(f'{final_result}!')
        else:
            print(f'{final_result}')
