#!/usr/bin/env python3
"""Main script for FizzBuzz."""
import sys

from fizzbuzz.game_starter import start_game
from fizzbuzz.logic import get_fizz_buzz


def main() -> None:
    """Run Fizz-Buzz."""
    try:
        start_game(get_fizz_buzz)
    except KeyboardInterrupt:
        sys.exit('\nGoodbye!')


if __name__ == '__main__':
    main()
