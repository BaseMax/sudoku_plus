# import pytest
from sudoku_plus import io, solver, generator, validator

def test_solver_solves_easy():
    """Test that the solver can solve a standard easy puzzle."""
    puzzle_str = (
        "530070000"  # row 1
        "600195000"  # row 2
        "098000060"  # row 3
        "800060003"  # row 4
        "400803001"  # row 5
        "700020006"  # row 6
        "060000280"  # row 7
        "000419005"  # row 8
        "000080079"  # row 9
    )
    puz = io.from_string(puzzle_str)
    sol = solver.solve(puz)
    assert sol is not None, "Solver failed to find a solution"
    assert validator.is_solution(puz, sol), "Solution is invalid"


def test_solver_preserves_clues():
    """Check that solver does not modify original clues."""
    puzzle_str = (
        "530070000"
        "600195000"
        "098000060"
        "800060003"
        "400803001"
        "700020006"
        "060000280"
        "000419005"
        "000080079"
    )
    puz = io.from_string(puzzle_str)
    sol = solver.solve(puz)
    for r in range(9):
        for c in range(9):
            if puz.grid[r][c] != 0:
                assert puz.grid[r][c] == sol.grid[r][c], "Solver changed a clue"


def test_generator_unique_solution():
    """Generated puzzles should have exactly one solution."""
    puz = generator.generate()
    count = solver.count_solutions(puz, limit=2)
    assert count == 1, "Generated puzzle does not have a unique solution"


def test_solver_returns_none_for_unsolvable():
    """Solver should return None for an invalid puzzle."""
    invalid_str = (
        "111111111"  # invalid puzzle: all 1s
        "111111111"
        "111111111"
        "111111111"
        "111111111"
        "111111111"
        "111111111"
        "111111111"
        "111111111"
    )
    puz = io.from_string(invalid_str)
    sol = solver.solve(puz)
    assert sol is None, "Solver should return None for unsolvable puzzle"
