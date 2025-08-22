from __future__ import annotations
from typing import Optional
from .grid import Sudoku, Coord
from . import strategies

def solve(board: Sudoku, max_solutions: int = 1):
    """
    Solve the given Sudoku. If max_solutions>1, return the number of solutions found (up to that cap).
    When max_solutions==1, returns a solved Sudoku or None.
    """
    if not board.is_valid():
        return None if max_solutions == 1 else 0

    # strategy pass
    s = board.copy()
    progress = True
    while progress:
        progress = False
        if strategies.fill_singles(s) > 0: progress = True
        if strategies.hidden_singles(s) > 0: progress = True

    if s.is_complete():
        return s if max_solutions == 1 else 1

    size = s.size
    best = None
    best_cands = None
    for coord in s.empty_cells():
        cs = s.candidates(coord.r, coord.c)
        if best is None or len(cs) < len(best_cands):  # type: ignore
            best = coord
            best_cands = cs
        if best_cands is not None and len(best_cands) == 1:
            break

    if best is None or not best_cands:
        return None if max_solutions == 1 else 0

    def constraint_score(val: int) -> int:
        r, c = best.r, best.c  # type: ignore
        score = 0
        for cc in range(size):
            if s.get(r, cc) == 0 and cc != c and val in s.candidates(r, cc):
                score += 1
        for rr in range(size):
            if s.get(rr, c) == 0 and rr != r and val in s.candidates(rr, c):
                score += 1
        br, bc = (r//s.box)*s.box, (c//s.box)*s.box
        for i in range(s.box):
            for j in range(s.box):
                rr, cc = br+i, bc+j
                if s.get(rr, cc) == 0 and (rr, cc) != (r, c) and val in s.candidates(rr, cc):
                    score += 1
        return score

    order = sorted(best_cands, key=constraint_score)

    if max_solutions == 1:
        for v in order:
            s2 = s.copy()
            s2.set(best.r, best.c, v)  # type: ignore
            res = solve(s2, max_solutions=1)
            if isinstance(res, Sudoku):
                return res
        return None
    else:
        count = 0
        for v in order:
            s2 = s.copy()
            s2.set(best.r, best.c, v)  # type: ignore
            res = solve(s2, max_solutions=max_solutions - count)
            if isinstance(res, Sudoku):
                count += 1
            elif isinstance(res, int):
                count += res
            if count >= max_solutions:
                break
        return count

def count_solutions(board: Sudoku, limit: int = 2) -> int:
    res = solve(board, max_solutions=limit)
    if isinstance(res, Sudoku):
        return 1
    return int(res or 0)
