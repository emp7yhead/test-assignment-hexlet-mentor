"""Game starter for FizzBuzz."""
import sys
from typing import Callable, Union

import prompt

GREETING_MSG = 'Welcome to Fizz Buzz!'
RULES_MSG = 'Submit a number and get an answer!'
ASK_NUMBER_MSG = 'Number: '


def start_game(game: Callable[[int], Union[str, int]]) -> None:
    """Start a game.

    Args:
        game: function that will be sented in infinite loop.
    """
    print(GREETING_MSG)
    print(RULES_MSG)
    while True:
        puzzled_number = prompt.string(ASK_NUMBER_MSG)
        try:
            final_result = game(int(puzzled_number))
        except ValueError:
            sys.exit('Please enter an integer!')
        if isinstance(final_result, str):
            print(f'{final_result}!')
        else:
            print(f'{final_result}')
