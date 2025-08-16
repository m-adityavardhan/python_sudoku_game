
# Python Sudoku Game

This is a graphical Sudoku game built with Python and Pygame. The game allows users to play, check their solution, reset the board, and auto-solve puzzles.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## How to Run
1. Clone the repository:
    ```powershell
    git clone https://github.com/m-adityavardhan/python_sudoku_game.git
    ```

2. Create and activate a Python virtual environment(recommended):
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. Install dependencies from requirements.txt:
   ```
   pip install -r requirements.txt
   ```
4. Run the game:
   ```
   python sudoku.py
   ```

## Features

- **Interactive GUI:** Play Sudoku with a clean, clickable interface.
- **Input Support:** Enter numbers using keyboard or mouse.
- **Check Solution:** Validate your current board for correctness.
- **Auto-Solve:** Instantly solve the puzzle using a backtracking algorithm.
- **Reset Board:** Start over with a new puzzle.
- **Visual Feedback:** "CORRECT", "WRONG", and "SUCCESS" messages for user actions.



## Controls

- **Number Keys (1-9):** Fill selected cell.
- **Delete Key:** Clear selected cell.
- **Enter Key / "Check" Button:** Validate current solution.
- **Spacebar / "Solve" Button:** Auto-solve the puzzle.
- **"Reset" Button:** Load a new puzzle.


