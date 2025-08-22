from __future__ import annotations
import argparse, sys, json
from . import generator, solver, io as sdio, validator
from .grid import Sudoku

def cmd_gen(args):
    puz = generator.generate(size=args.size, symmetry=not args.no_symmetry, difficulty=args.difficulty, min_clues=args.min_clues)
    if args.format == "string":
        print(sdio.to_string(puz))
    else:
        print(puz)
    if args.rate:
        print(json.dumps(generator.rate(puz), indent=2))

def _read_puzzle(arg: str, size: int) -> Sudoku:
    data = sys.stdin.read().strip() if arg == "-" else arg.strip()
    return sdio.from_string(data, size=size)

def cmd_solve(args):
    puz = _read_puzzle(args.puzzle, args.size)
    res = solver.solve(puz)
    if res is None:
        print("No solution found", file=sys.stderr)
        sys.exit(1)
    if args.format == "string":
        print(sdio.to_string(res))
    else:
        print(res)

def cmd_rate(args):
    puz = _read_puzzle(args.puzzle, args.size)
    print(json.dumps(generator.rate(puz), indent=2))

def cmd_validate(args):
    puz = _read_puzzle(args.puzzle, args.size)
    sol = _read_puzzle(args.solution, args.size)
    ok = validator.is_solution(puz, sol)
    print("OK" if ok else "INVALID")
    sys.exit(0 if ok else 2)

def main(argv=None):
    p = argparse.ArgumentParser(prog="sudoku", description="Sudoku generator/solver CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("gen", help="Generate a puzzle")
    g.add_argument("--size", type=int, default=9, choices=[4,9,16])
    g.add_argument("--difficulty", default="medium", choices=["easy","medium","hard"])
    g.add_argument("--min-clues", type=int, default=24)
    g.add_argument("--no-symmetry", action="store_true")
    g.add_argument("--format", choices=["ascii","string"], default="ascii")
    g.add_argument("--rate", action="store_true", help="Also print difficulty rating JSON")
    g.set_defaults(func=cmd_gen)

    s = sub.add_parser("solve", help="Solve a puzzle from a string or '-' for stdin")
    s.add_argument("puzzle")
    s.add_argument("--size", type=int, default=9, choices=[4,9,16])
    s.add_argument("--format", choices=["ascii","string"], default="ascii")
    s.set_defaults(func=cmd_solve)

    r = sub.add_parser("rate", help="Rate a puzzle difficulty")
    r.add_argument("puzzle")
    r.add_argument("--size", type=int, default=9, choices=[4,9,16])
    r.set_defaults(func=cmd_rate)

    v = sub.add_parser("validate", help="Validate a solution for a puzzle")
    v.add_argument("puzzle")
    v.add_argument("solution")
    v.add_argument("--size", type=int, default=9, choices=[4,9,16])
    v.set_defaults(func=cmd_validate)

    args = p.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    main()