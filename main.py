#!/usr/bin/env python3
import argparse
from sudoku.generator import generate_sudoku
from sudoku.solver import solve_sudoku, is_valid_board
from sudoku.utils import print_board


def run_generate(size: int):
    print(f"🔢 Generating a {size}x{size} Sudoku puzzle...\n")
    board = generate_sudoku(size)
    print_board(board)


def run_solve(board_str: str):
    print("🧩 Solving Sudoku...\n")
    # Convert comma/space separated string into board
    rows = [list(map(int, row.split(","))) for row in board_str.split(";")]
    solved = solve_sudoku(rows)

    if solved:
        print("✅ Solution found:\n")
        print_board(solved)
    else:
        print("❌ No solution exists for the provided board.")


def run_validate(board_str: str):
    print("🔍 Validating Sudoku board...\n")
    rows = [list(map(int, row.split(","))) for row in board_str.split(";")]
    valid = is_valid_board(rows)

    if valid:
        print("✅ The board is valid!")
    else:
        print("❌ The board is invalid!")


def main():
    parser = argparse.ArgumentParser(
        description="Sudoku Generator, Solver, and Validator"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate a Sudoku puzzle")
    gen_parser.add_argument(
        "--size", type=int, default=9, help="Board size (default: 9)"
    )

    # Solve command
    solve_parser = subparsers.add_parser("solve", help="Solve a Sudoku puzzle")
    solve_parser.add_argument(
        "--board",
        type=str,
        required=True,
        help='Board as string, rows separated by ";" and values by "," (use 0 for empty). '
             'Example: "5,3,0,0,7,0,0,0,0;6,0,0,1,9,5,0,0,0;0,9,8,0,0,0,0,6,0;..."'
    )

    val_parser = subparsers.add_parser("validate", help="Validate a Sudoku puzzle")
    val_parser.add_argument(
        "--board",
        type=str,
        required=True,
        help='Same format as solve command.'
    )

    args = parser.parse_args()

    if args.command == "generate":
        run_generate(args.size)
    elif args.command == "solve":
        run_solve(args.board)
    elif args.command == "validate":
        run_validate(args.board)


if __name__ == "__main__":
    main()
