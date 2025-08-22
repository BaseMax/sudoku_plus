from __future__ import annotations
from .grid import Sudoku

def is_solution(puzzle: Sudoku, solution: Sudoku) -> bool:
    """Check solution matches puzzle clues and is valid/complete."""
    if puzzle.size != solution.size:
        return False
    n = puzzle.size
    for r in range(n):
        for c in range(n):
            if puzzle.get(r,c) and puzzle.get(r,c) != solution.get(r,c):
                return False
    return solution.is_complete() and solution.is_valid()
