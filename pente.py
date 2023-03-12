from datetime import datetime
from typing import List, Optional, Tuple


BOARD_SIZE = 19


class Pente:
    # Static variable for all possible directions to check: R, RD, D, LD, L, LU, U, RU
    directions: List[Tuple[int, int]] = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    def __init__(self, save_moves: bool = False) -> None:
        self.board: List[List[str]] = [
            ["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
        ]
        self.current_player: str = "X"
        self.opponent: str = "O"
        self.winner: Optional[str] = None
        self.game_over: bool = False
        self.num_opponent_captures: int = 0
        self.num_current_player_captures: int = 0
        self.save_moves: bool = save_moves
        self.moves: List[Tuple[int, int]] = []

    def print_board(self) -> None:
        # Print top border
        print("   " + " ".join([f"{i:2}" for i in range(BOARD_SIZE)]))
        print(" +" + "-" * (BOARD_SIZE * 3 - 1) + "+")

        # Print board rows with row numbers every 5th row
        for i, row in enumerate(self.board):
            print(f"{i:2}|", end="")

            for cell in row:
                print(f" {cell} ", end="")
            print("|")

        # Print bottom border and current capture numbers
        print(" +" + "-" * (BOARD_SIZE * 3 - 1) + "+")
        print(
            f"Captures: {self.current_player}={self.num_current_player_captures}, {self.opponent}={self.num_opponent_captures}"
        )

    def place_stone(self, x: int, y: int) -> bool:
        if self.board[x][y] != ".":
            return False
        self.board[x][y] = self.current_player
        self.check_for_captures(x, y)
        self.check_for_win(x, y)
        self.current_player, self.opponent = self.opponent, self.current_player

        self.moves.append((x, y))
        return True

    def check_for_captures(self, x: int, y: int) -> None:
        # All possible directions to check for captures R, RD, D, LD, L, LU, U, RU
        for dx, dy in Pente.directions:
            captured_stones = self.check_capture(x, y, dx, dy)
            if captured_stones:
                self.remove_captured_stones(captured_stones)

    def check_capture(self, x: int, y: int, dx: int, dy: int) -> List[Tuple[int, int]]:
        captured_stones = []
        num_opponent_stones = 0
        i, j = x + dx, y + dy
        while (
            i >= 0
            and i < BOARD_SIZE
            and j >= 0
            and j < BOARD_SIZE
            and self.board[i][j] == self.opponent
        ):
            num_opponent_stones += 1
            captured_stones.append((i, j))
            i += dx
            j += dy

        if (
            num_opponent_stones == 2
            and i >= 0
            and i < BOARD_SIZE
            and j >= 0
            and j < BOARD_SIZE
            and self.board[i][j] == self.current_player
        ):
            self.num_opponent_captures += 2
            return captured_stones
        return []

    def remove_captured_stones(self, captured_stones: List[Tuple[int, int]]) -> None:
        for i, j in captured_stones:
            self.board[i][j] = "."

    def check_for_win(self, x: int, y: int) -> None:
        if self.check_five_in_a_row(x, y):
            self.winner = self.current_player
            self.game_over = True
        elif self.num_opponent_captures >= 10:
            self.winner = self.current_player
            self.game_over = True
        elif self.num_current_player_captures >= 10:
            self.winner = self.opponent
            self.game_over = True

    def check_five_in_a_row(self, x: int, y: int) -> bool:
        for dx, dy in Pente.directions:
            count: int = 1
            i: int
            j: int
            i, j = x + dx, y + dy
            while (
                i >= 0
                and i < BOARD_SIZE
                and j >= 0
                and j < BOARD_SIZE
                and self.board[i][j] == self.current_player
            ):
                count += 1
                i += dx
                j += dy

            if count >= 5:
                return True
        return False

    def make_move(self, x: int, y: int) -> None:
        if not self.game_over:
            if self.place_stone(x, y):
                self.print_board()
                print(f"{self.winner} wins!")

            else:
                print("Invalid move. Try again.")
        else:
            print("Game over.")

    def save_moves_to_file(self) -> None:
        # Save the moves to a file
        game_str = ";".join([f"{x},{y}" for x, y in self.moves])
        filename = f"moves-{datetime.now()}.txt"
        print(f"Saving game to {filename} with moves {game_str}")
        with open(filename, "w") as f:
            f.write(game_str)

        print("Saved!")
