import pytest

from pySnake.snake import Snake


@pytest.fixture
def s() -> Snake:
    return Snake()


def test_pause(s):
    assert not s.pause


def test_step(s):
    assert s.snake_step == 20


def test_default_snake_segments(s: Snake):
    assert len(s.snake_segments) == 3





