# Python Pente Game Engine

Pente is a two-player board game played on a 19x19 grid, similar to tic-tac-toe. The goal of the game is to get 5 in a row (vertical, horizontal, or diagonal), or to capture 10 of your opponent's stones.

## Playing the Game

Players take turns placing stones on the board, with X and O representing the two players. Stones can be placed anywhere on the board as long as the cell is not already occupied. Captures are made by flanking two of your opponent's stones with your stones, horizontally, vertically or diagonally. Captured stones are removed from the board, and the open spots can be played again. A capture is only performed if the player doing the capture is the last to play.

## Implementation
The Pente game has been implemented in Python, with the ability to play the game interactively or input a string of moves to simulate a game. A command line utility is provided to wrap the game and provide an interactive interface. The game board is printed to the console with row and column numbers. The Pente game will in the future also include a simple AI algorithm that can be used to play against the computer.

### The Game Engine

The game engine is implemented in the `game_engine.py` file, and all the logic is encapsulated inside the `Pente` class. The game board itself is represented by a 19 by 19 two-dimensional array of strings where "." is an empty cell, "X" means player one, and "O" means player two. The `Pente` class has the following important methods:

- `__init__(self, save_moves: bool = False) -> None`: Initializes the game board and sets the current player to X.
- `place_stone(self, x: int, y: int) -> bool`: Places a stone at the given coordinates. Returns True if the move was successful, and False otherwise.
- `check_for_captures(self, x: int, y: int) -> None`: Checks if the given move resulted in a capture. If so, the captured stones are removed from the board.
- `check_for_win(self, x: int, y: int) -> None`: Checks if the given move resulted in a win. If so, marks the game as over.
- `check_five_in_a_row(self, x: int, y: int) -> bool`: Subroutine of `check_for_win` that checks if the last move resulted in either player getting 5 in a row.


### A Word on the Notation

In official tournaments, they use the same system as chess to denote moves. In this version, however, I have chosen to use a simpler notation where the coordinates are separated by a comma. For example, the move "A1" would be represented as "0,0" and the move "T19" would be represented as "18,18". This is because the game board is represented by a two-dimensional array, and it is easier to access the cells using the coordinates as indices.

A full game is represented by a string of moves separated by semicolons. For example, the following string represents a game where player X plays the first move at A1, and player O plays the second move at B1:

```python
"0,0;1,0"
```

In the future, we want to support both notations, but for now, we will stick with the simpler notation.

A more detailed description of the notation can be found in the [Wikipedia article](https://en.wikipedia.org/wiki/Pente#Notation).


## Installation
To play the Pente game, you need to have Python 3 installed on your system. Clone the repository and install the required packages by running (preferably in a virtual environment):

```shell
# Clone the repository
git clone https://github.com/ankile/play-pente.git
cd play-pente

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

## Usage
To play the game interactively, run:

```python
python pente.py --interactive
# or
python pente.py -i
```

If you want to save the game to a file after the game has concluded, run:

```python
python pente.py --interactive --save
# or
python pente.py -i -s
```

To input a string of moves, run:

```python
python pente.py --moves "x1,y1;x2,y2;..."
# or
python pente.py -m "x1,y1;x2,y2;..."
```

A file that has been saved previously can also be loaded and played:

```python
python pente.py --file "path/to/file"
# or
python pente.py -f "path/to/file"
```

Use the --help option to see a list of all available options:

```python
python pente.py --help
```

## Testing
To run the test suite, you need to have `pytest` installed. You can run either of the following commands from the root of the repository:

```python
python -m pytest tests.py
# and
python pente.py --test
# or
python pente.py -t
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.



