# Sudoku Plus 🧩

A complete **Sudoku toolkit in Python** featuring:

- Sudoku board generator
- Sudoku solver (backtracking + optional advanced heuristics)
- Validator (check if a Sudoku is valid)
- CLI interface for generating and solving puzzles
- Test suite for all modules

---

## 📂 Project Structure

```
sudoku_plus/
│── src/
│   └── sudoku_plus/
│       ├── __init__.py
│       ├── board.py
│       ├── generator.py
│       ├── solver.py
│       ├── validator.py
│       └── cli.py
│
│── tests/
│   ├── test_board.py
│   ├── test_generator.py
│   ├── test_solver.py
│   ├── test_validator.py
│
│── main.py
│── requirements.txt
│── README.md
````

---

## ⚡ Installation

Clone this repository:

```bash
git clone https://github.com/BaseMax/SudokuPython.git
cd SudokuPython
````

(Optional) Create a virtual environment:

```bash
python3 -m venv venv
```

On Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

## Install your project in editable mode

From project root:

```bash
pip install -e .
```

> `-e` = editable → you can edit source code without reinstalling.

After this, sudoku_plus is recognized as a proper Python package.

## Run your CLI anywhere

Now you can do:

```bash
python -m sudoku_plus.cli gen --size 9 --difficulty medium
```

Or, because we added [project.scripts], you can also run directly:

```bash
sudoku gen --size 9 --difficulty medium
```

---

### 🔹 Generate a Sudoku Puzzle

```bash
python -m sudoku_plus.cli gen --size 9 --difficulty medium
```

* `--size` → board size (default: 9)
* `--difficulty` → `easy | medium | hard`

Example:

```bash
python -m sudoku_plus.cli gen --size 9 --difficulty hard
```

---

### 🔹 Solve a Sudoku Puzzle

Provide a puzzle as a string (`0` = empty):

```bash
python -m sudoku_plus.cli solve "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
```

Or read from file:

```bash
python -m sudoku_plus.cli solve --file puzzle.txt
```

---

### 🔹 Validate a Sudoku Board

```bash
python -m sudoku_plus.cli validate <puzzle_string> <solution_string>
```

For example:

```bash
python -m sudoku_plus.cli validate "530070000600195000098000060800060003400803001700020006060000280000419005000080079" "534678912672195348198342567859761423426853791713924856961537284287419635345286179"
```

---

## 🧪 Running Tests

Tests are written with `pytest`.
To run all tests:

```bash
pytest tests/
```

Run a specific test file:

```bash
pytest tests/test_solver.py
```

---

## ✨ Features Roadmap

* [x] Basic solver (backtracking)
* [x] Random puzzle generator
* [x] CLI interface
* [x] Test suite
* [ ] GUI visualizer (Tkinter/PyGame)
* [ ] Advanced solving strategies (human-like techniques)
* [ ] Export puzzles to `.txt` / `.csv`

---

## 📜 License

MIT License © 2025 [BaseMax](https://github.com/BaseMax)
