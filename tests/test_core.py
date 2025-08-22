import pytest
from sudoku_plus import io, solver, generator, validator

def test_solver_solves_easy():
    puz = io.from_string("53..7....6..195....98....6.8...6...34..8.3..17...2...6....28....419..5....8..79")
    sol = solver.solve(puz)
    assert sol is not None
    assert validator.is_solution(puz, sol)

def test_generator_unique():
    puz = generator.generate()
    count = solver.count_solutions(puz, limit=2)
    assert count == 1
