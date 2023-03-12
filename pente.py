import argparse
import time

import pytest

from game_engine import BOARD_SIZE, Pente


def main():
    parser = argparse.ArgumentParser(description="Play Pente!")
    parser.add_argument(
        "-i", "--interactive", action="store_true", help="Play in interactive mode"
    )
    parser.add_argument(
        "-s",
        "--save",
        action="store_true",
        help="Write the move history after the game",
    )
    parser.add_argument(
        "-m",
        "--moves",
        help='Provide a string of moves to play (format: "x1,y1;x2,y2;...")',
    )
    parser.add_argument(
        "-f",
        "--file",
        help='Provide a path to a file containing moves to play (format: "x1,y1;x2,y2;...")',
    )
    parser.add_argument(
        "-v",
        "--visualize",
        action="store_true",
        help="Show the board as it is played in non-interactive mode",
    )
    # Add argument to run the tests
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="Run the tests",
    )

    args = parser.parse_args()

    if args.interactive:
        play_interactive(save_moves=args.save)
    elif args.moves:
        play_moves(args.moves, visualize=args.visualize)
    elif args.file:
        with open(args.file, "r") as f:
            play_moves(f.read(), visualize=args.visualize)
    elif args.test:
        # Run the tests with pytest
        pytest.main(["-v", "tests.py"])
    else:
        print("Please choose either interactive mode or provide a string of moves.")


def play_interactive(save_moves=False):
    game = Pente(save_moves=save_moves)
    print("Welcome to Pente!")
    game.print_board()
    while not game.game_over:
        try:
            x, y = input(
                f"{game.current_player}, enter x and y coordinates separated by a space (e.g. '3 5'): "
            ).split()
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        if not x.isdigit() or not y.isdigit():
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        x = int(x)
        y = int(y)
        if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
            print(
                f"Invalid move. The x and y coordinates must be between 0 and {BOARD_SIZE - 1}."
            )
            continue
        if not game.place_stone(x, y):
            print("Invalid move. That cell is already occupied.")
            continue
        game.print_board()
        if game.game_over:
            print(f"{game.winner} wins!")

    if save_moves:
        game.save_moves_to_file()


def play_moves(moves_str: str, visualize: bool = False) -> None:
    game = Pente()
    for move_str in moves_str.split(";"):
        x, y = move_str.split(",")
        x = int(x)
        y = int(y)
        if not game.place_stone(x, y):
            print(f"Invalid move: {move_str}")
            return

        if visualize:
            game.print_board()
            time.sleep(1)

    print(f"{game.winner} wins!")


if __name__ == "__main__":
    main()
