from __future__ import annotations
import random
from .grid import Sudoku
from .solver import count_solutions

def _make_full_solution(size: int = 9) -> Sudoku:
    """Create a fully solved grid by randomized backtracking."""
    s = Sudoku(size=size)
    nums = list(range(1, size+1))
    def backtrack(pos: int = 0) -> bool:
        if pos == size*size:
            return True
        r, c = divmod(pos, size)
        if s.get(r,c) != 0:
            return backtrack(pos+1)
        random.shuffle(nums)
        for v in nums:
            if v in s.row_values(r) or v in s.col_values(c) or v in s.box_values(r,c):
                continue
            s.set(r,c,v)
            if backtrack(pos+1):
                return True
            s.set(r,c,0)
        return False
    backtrack(0)
    return s

def generate(size: int = 9, symmetry: bool = True, difficulty: str = "medium", min_clues: int = 24) -> Sudoku:
    """Generate a puzzle with a unique solution. Difficulty influences clue removal."""
    full = _make_full_solution(size=size)
    puzzle = full.copy()
    indices = list(range(size*size))
    random.shuffle(indices)

    diff_factor = {"easy": 0.45, "medium": 0.6, "hard": 0.7}.get(difficulty, 0.6)
    target_removed = int(size*size*diff_factor)

    def remove_pair(idx: int):
        r, c = divmod(idx, size)
        rr, cc = r, c
        symm = (size-1-r, size-1-c)
        puzzle.set(rr, cc, 0)
        if symmetry and (rr,cc) != symm:
            puzzle.set(symm[0], symm[1], 0)

    removed = 0
    for idx in indices:
        if removed >= target_removed:
            break
        backup = [row[:] for row in puzzle.grid]
        remove_pair(idx)
        if count_solutions(puzzle, limit=2) != 1:
            puzzle.grid = backup
        else:
            removed = sum(1 for r in range(size) for c in range(size) if puzzle.get(r,c) == 0)
        clues = size*size - removed
        if clues < min_clues:
            puzzle.grid = backup
            break
    return puzzle

def rate(puzzle: Sudoku) -> dict:
    from . import strategies
    s = puzzle.copy()
    singles = strategies.fill_singles(s)
    hidden = strategies.hidden_singles(s)
    pairs = strategies.naked_pairs(s)
    needs_bt = 0
    if not s.is_complete():
        empties = list(s.empty_cells())
        if empties:
            mrv = min((len(s.candidates(rc.r, rc.c)) for rc in empties))
            needs_bt = mrv
    score = singles*1 + hidden*2 + pairs*3 + needs_bt*5
    level = "easy" if score < 20 else "medium" if score < 45 else "hard"
    return {"score": score, "level": level, "features": {"singles": singles, "hidden": hidden, "naked_pairs": pairs, "mrv": needs_bt}}
