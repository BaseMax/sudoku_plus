from __future__ import annotations
from dataclasses import dataclass
from typing import List, Iterable

@dataclass(frozen=True)
class Coord:
    r: int
    c: int

class Sudoku:
    """A size x size Sudoku (default 9). Box size must square to size (e.g., 3 for 9x9)."""
    def __init__(self, size: int = 9):
        self.size = size
        self.box = int(self.size ** 0.5)
        if self.box * self.box != self.size:
            raise ValueError("size must be a perfect square (4, 9, 16, ...)")
        self.grid: List[List[int]] = [[0]*self.size for _ in range(self.size)]

    @classmethod
    def from_rows(cls, rows: Iterable[Iterable[int]]) -> "Sudoku":
        rows = [list(r) for r in rows]
        size = len(rows)
        s = cls(size=size)
        if any(len(r) != size for r in rows):
            raise ValueError("rows must form a square")
        s.grid = [list(r) for r in rows]
        return s

    def copy(self) -> "Sudoku":
        s = Sudoku(self.size)
        s.grid = [row[:] for row in self.grid]
        return s

    def set(self, r: int, c: int, val: int) -> None:
        self.grid[r][c] = val

    def get(self, r: int, c: int) -> int:
        return self.grid[r][c]

    def empty_cells(self) -> Iterable[Coord]:
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    yield Coord(r, c)

    def row_values(self, r: int) -> set[int]:
        return set(v for v in self.grid[r] if v)

    def col_values(self, c: int) -> set[int]:
        return set(self.grid[r][c] for r in range(self.size) if self.grid[r][c])

    def box_values(self, r: int, c: int) -> set[int]:
        br = (r // self.box) * self.box
        bc = (c // self.box) * self.box
        vals = set()
        for i in range(self.box):
            for j in range(self.box):
                v = self.grid[br + i][bc + j]
                if v:
                    vals.add(v)
        return vals

    def candidates(self, r: int, c: int) -> set[int]:
        if self.grid[r][c] != 0:
            return set()
        used = self.row_values(r) | self.col_values(c) | self.box_values(r, c)
        return set(range(1, self.size + 1)) - used

    def is_complete(self) -> bool:
        return all(all(v != 0 for v in row) for row in self.grid)

    def is_valid(self) -> bool:
        # rows and cols no duplicates (ignoring zeros)
        for i in range(self.size):
            row = [v for v in self.grid[i] if v]
            col = [self.grid[r][i] for r in range(self.size) if self.grid[r][i]]
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False
        # box duplicates
        for br in range(0, self.size, self.box):
            for bc in range(0, self.size, self.box):
                boxvals = []
                for i in range(self.box):
                    for j in range(self.box):
                        v = self.grid[br + i][bc + j]
                        if v: boxvals.append(v)
                if len(boxvals) != len(set(boxvals)):
                    return False
        return True

    def __str__(self) -> str:
        out = []
        for r in range(self.size):
            line = []
            for c in range(self.size):
                v = self.grid[r][c]
                line.append(str(v) if v else ".")
                if (c+1) % self.box == 0 and c+1 != self.size:
                    line.append("|")
            out.append(" ".join(line))
            if (r+1) % self.box == 0 and r+1 != self.size:
                out.append("-" * (len(out[-1])))
        return "\n".join(out)
