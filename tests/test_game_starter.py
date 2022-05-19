"""Test for game_starter.py."""
import pytest

from fizzbuzz.game_starter import start_game


def test_start_game_str_input(monkeypatch):
    """Test string input.

    Args:
        monkeypatch: using for monkeypatching input.
    """
    monkeypatch.setattr('builtins.input', lambda _: 'hey')
    with pytest.raises(SystemExit):
        start_game('random_string_to_trigger_test')
