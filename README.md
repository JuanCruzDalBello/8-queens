# 8-queens
Script to solve the 8 queens problem.

## Usage
python queens.py

Shows on terminal the representation of the solution to the problem, along with the position of all the queens on the board.

## Logic
The 8 queens problems proposes placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other, so a solution requires that no two queens share the same row, column, or diagonal.

The script uses backingtrack to solve the problem.

First checks if all queens are already on the board, if so the function returns True, as the board is already complete.
If there are still queens left to be placed, it iterates through the board searching for a space where the next queen could be positioned, if the space is valid (this being if the queen placed there would not threaten another one) the queen is placed there, and the function is called again in a recursive manner.
