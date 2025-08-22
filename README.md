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
sudoku\_plus/
---- src
    │── sudoku\_plus/
    │   ├── **init**.py
    │   ├── board.py       # Sudoku board representation & utilities
    │   ├── generator.py   # Puzzle generator
    │   ├── solver.py      # Solver algorithms
    │   ├── validator.py   # Validator for checking correctness
    │   └── cli.py         # Command line interface
    │
│── tests/
│   ├── test\_board.py
│   ├── test\_generator.py
│   ├── test\_solver.py
│   ├── test\_validator.py
│
│── main.py            # Entry point (runs CLI)
│── requirements.txt   # Dependencies (if any)
│── README.md          # Documentation
````

---

## ⚡ Installation

Clone this repository:

```bash
git clone https://github.com/BaseMax/SudokuPython.git
cd SudokuPython/sudoku_plus
````

(Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### Run the CLI

```bash
python main.py
```

This will start the interactive CLI where you can choose:

* Generate a Sudoku puzzle
* Solve an existing Sudoku
* Validate a Sudoku board
* Print puzzles in terminal

---

### 🔹 Generate a Sudoku Puzzle

```bash
python -m sudoku.generator --size 9 --difficulty medium
```

* `--size` → board size (default: 9)
* `--difficulty` → `easy | medium | hard`

Example:

```bash
python -m sudoku.generator --size 9 --difficulty hard
```

---

### 🔹 Solve a Sudoku Puzzle

Provide a puzzle as a string (`0` = empty):

```bash
python -m sudoku.solver "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
```

Or read from file:

```bash
python -m sudoku.solver --file puzzle.txt
```

---

### 🔹 Validate a Sudoku Board

```bash
python -m sudoku.validator "valid_puzzle_string"
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
