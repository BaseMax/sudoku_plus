from __future__ import annotations
from .grid import Sudoku

def fill_singles(s: Sudoku) -> int:
    """Fill cells that have exactly one candidate. Returns count filled."""
    filled = 0
    progress = True
    while progress:
        progress = False
        for r in range(s.size):
            for c in range(s.size):
                if s.get(r,c) == 0:
                    cand = s.candidates(r,c)
                    if len(cand) == 1:
                        s.set(r,c,next(iter(cand)))
                        filled += 1
                        progress = True
    return filled

def hidden_singles(s: Sudoku) -> int:
    """If a number only appears as candidate once in a unit (row/col/box), place it."""
    n = s.size
    placed = 0
    # Rows
    for r in range(n):
        needed = {k: [] for k in range(1, n+1)}
        for c in range(n):
            if s.get(r,c) == 0:
                for k in s.candidates(r,c):
                    needed[k].append((r,c))
        for k, cells in needed.items():
            if len(cells) == 1:
                rr, cc = cells[0]
                if s.get(rr,cc) == 0:
                    s.set(rr,cc,k)
                    placed += 1
    # Cols
    for c in range(n):
        needed = {k: [] for k in range(1, n+1)}
        for r in range(n):
            if s.get(r,c) == 0:
                for k in s.candidates(r,c):
                    needed[k].append((r,c))
        for k, cells in needed.items():
            if len(cells) == 1:
                rr, cc = cells[0]
                if s.get(rr,cc) == 0:
                    s.set(rr,cc,k)
                    placed += 1
    # Boxes
    b = s.box
    for br in range(0, n, b):
        for bc in range(0, n, b):
            needed = {k: [] for k in range(1, n+1)}
            for i in range(b):
                for j in range(b):
                    r, c = br+i, bc+j
                    if s.get(r,c) == 0:
                        for k in s.candidates(r,c):
                            needed[k].append((r,c))
            for k, cells in needed.items():
                if len(cells) == 1:
                    rr, cc = cells[0]
                    if s.get(rr,cc) == 0:
                        s.set(rr,cc,k)
                        placed += 1
    return placed

def naked_pairs(s: Sudoku) -> int:
    """Eliminate candidates using naked pair rule; returns number of eliminations (for rating)."""
    n = s.size
    # Helper unit processing returns eliminations count by simulation (no persistent candidate store).
    def process(cells):
        elims = 0
        cands = []
        for (r,c) in cells:
            if s.get(r,c) == 0:
                cands.append(((r,c), s.candidates(r,c)))
        pairs = {}
        for rc, cs in cands:
            if len(cs) == 2:
                key = tuple(sorted(cs))
                pairs.setdefault(key, []).append(rc)
        for pair, rcs in pairs.items():
            if len(rcs) == 2:
                for rc, cs in cands:
                    if rc not in rcs:
                        elims += len(cs.intersection(pair))
        return elims
    total = 0
    for r in range(n):
        total += process([(r,c) for c in range(n)])
    for c in range(n):
        total += process([(r,c) for r in range(n)])
    b = s.box
    for br in range(0, n, b):
        for bc in range(0, n, b):
            cells = [(br+i, bc+j) for i in range(b) for j in range(b)]
            total += process(cells)
    return total
