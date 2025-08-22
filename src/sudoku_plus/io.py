from __future__ import annotations
from typing import Iterable, List
from .grid import Sudoku

def from_string(s: str, size: int = 9) -> Sudoku:
    """Load puzzle from a compact string with . or 0 for blanks (length = size*size)."""
    s = "".join(ch for ch in s if not ch.isspace())
    if len(s) != size*size:
        raise ValueError(f"expected {size*size} chars, got {len(s)}")
    rows: List[List[int]] = []
    for i in range(0, len(s), size):
        row = []
        for ch in s[i:i+size]:
            row.append(0 if ch in ".0" else int(ch))
        rows.append(row)
    return Sudoku.from_rows(rows)

def to_string(board: Sudoku) -> str:
    return "".join(str(board.get(r,c) or ".") for r in range(board.size) for c in range(board.size))

def from_rows(rows: Iterable[Iterable[int]]) -> Sudoku:
    return Sudoku.from_rows(rows)
