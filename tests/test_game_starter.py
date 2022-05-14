"""Test for game_starter.py"""
import pytest

from fizzbuzz.game_starter import start_game


@pytest.fixture
def game_fixture():
    pass


def test_start_game_str_input(monkeypatch, game_fixture):
    """Test input with string input."""
    monkeypatch.setattr('builtins.input', lambda _: 'hey')
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        start_game(game_fixture)
    assert pytest_wrapped_e.type == SystemExit
