# import pytest
from sudoku_plus import io, solver, generator, validator

def test_solver_solves_easy():
    puz = io.from_string(
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
    sol = solver.solve(puz)
    assert sol is not None
    assert validator.is_solution(puz, sol)

def test_generator_unique():
    puz = generator.generate()
    count = solver.count_solutions(puz, limit=2)
    assert count == 1
