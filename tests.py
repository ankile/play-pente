import pytest

from pente import Pente, BOARD_SIZE


@pytest.fixture
def game():
    return Pente()


def test_place_stone(game):
    assert game.place_stone(0, 0) == True
    assert game.place_stone(0, 0) == False
    assert game.place_stone(1, 0) == True
    assert game.place_stone(0, 1) == True


def test_capture_stones(game):
    game.place_stone(0, 0)  # X
    game.place_stone(1, 0)  # O
    game.place_stone(0, 1)  # X
    game.place_stone(2, 0)  # O
    game.place_stone(3, 0)  # X

    print(game.board[:4])

    assert [row[:3] for row in game.board[:4]] == [
        ["X", "X", "."],
        [".", ".", "."],
        [".", ".", "."],
        ["X", ".", "."],
    ]
    assert game.num_current_player_captures == 0
    assert game.num_opponent_captures == 2


def test_check_win(game):
    game.place_stone(0, 0)
    game.place_stone(1, 0)
    game.place_stone(0, 1)
    game.place_stone(2, 0)
    game.place_stone(0, 2)
    game.place_stone(3, 0)
    game.place_stone(0, 3)
    game.place_stone(4, 0)
    game.place_stone(0, 4)
    assert game.game_over == True
    assert game.winner == "X"
