# Personal Expense Tracker with CSV

A beginner-friendly command-line expense tracker written in Python. It records daily expenses by category, stores them persistently in a CSV file, and generates category summary statistics.

Built as a practice project to learn structured data storage and file I/O operations with the `csv` module.

## Features

- **Add expenses** — every entry stores the date (auto-filled with today), a category, the amount, and an optional short description. Suggested categories are offered, and custom ones are allowed after a prompt.
- **View all expenses** — prints a formatted table of every recorded entry.
- **Filter expenses** — narrow the list by:
  - Category (e.g. show only `food`)
  - Exact date (`YYYY-MM-DD`, real date validation)
  - Minimum amount (e.g. everything of 7.00 or more)
- **Category summary statistics** — entries, total amount spent, and percentage share per category, a grand total, and the category you spent the most on.
- **Persistent CSV storage** — expenses are saved to `expenses.csv` using the `csv` module; the file is created automatically on the first entry and reloaded on the next run.
- **Input validation** — every prompt uses a `while` loop, so invalid amounts, empty categories, or bad menu choices never crash the program.

## Getting Started

### Prerequisites

- Python 3 installed on your machine (no external libraries required).

### Running the Program

1. Clone the repository:

   ```bash
   git clone https://github.com/Divyanshu11007/Personal-Expense-Tracker-with-CSV.git
   cd Personal-Expense-Tracker-with-CSV
   ```

2. Run the program:

   ```bash
   python expense_tracker.py
   ```

## How It Works

The program opens with a main menu:

```
========================================
     Personal Expense Tracker (CSV)
========================================

MAIN MENU
1. Add expense
2. View all expenses
3. Filter expenses
4. Category summary
5. Exit
Choose an option (1-5):
```

Pick an option from `1` to `5`. All entries stay saved in `expenses.csv` between runs. Keep this file in the same folder as the script.

## Example Session

```
--- Add Expense ---
Suggested categories: food, transport, books, shopping, health, other
Enter the expense category (blank = other): food
Enter the amount spent: 12.50
Short description (optional): lunch with coffee

Saved food expense of 12.50 on 2026-10-31. (Total entries: 1)
```

```
--- Category Summary ---

Category       Entries       Total   Share
--------------------------------------------
food                2       19.75   79.8%
transport           1        5.00   20.2%
--------------------------------------------
GRAND TOTAL         3       24.75

You spent the most on: food (19.75)
```

## Notes

- `expenses.csv` is your personal data file and is intentionally **not** tracked by git (see `.gitignore`), so the repository stays clean while your real expenses stay private.
- The CSV is rewritten whenever an expense is added — a simple demo of structured file writing with the `csv` module.
- The program reads the CSV into a list when it starts; changes made externally while the program is running are not picked up until the next launch.

## Project Goal

This project demonstrates:

- CSV reading and writing with the `csv` module (`csv.DictReader` / `csv.DictWriter`)
- Persistent, structured data storage in files
- Lists of dictionaries for tabular data
- Dictionaries for totalling and statistics (`sum`, `max`, `sorted`)
- Date handling with the `datetime` module (`date.today`, `date.fromisoformat`)
- `while` loops, functions, and input validation
- List comprehensions for filtering data

## License

This project is free to use and modify for learning purposes.
