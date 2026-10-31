import csv
import os
from datetime import date

CSV_FILE = "expenses.csv"
CSV_HEADER = ["Date", "Category", "Amount", "Description"]

SUGGESTED_CATEGORIES = ["food", "transport", "books", "shopping", "health", "other"]


def get_amount(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
        except ValueError:
            print("Please enter a valid amount (e.g. 12.50).")
            continue
        if amount <= 0:
            print("The amount must be greater than zero.")
            continue
        return amount


def get_category():
    print("Suggested categories: " + ", ".join(SUGGESTED_CATEGORIES))
    while True:
        category = input("Enter the expense category (blank = other): ").strip().lower()
        if category == "":
            return "other"
        if category not in SUGGESTED_CATEGORIES:
            confirm = input(f"'{category}' is not in the suggested list. Save anyway? (y/n): ").strip().lower()
            if confirm not in ("y", "yes"):
                continue
        return category


def get_filter_text(prompt):
    while True:
        text = input(prompt).strip().lower()
        if text != "":
            return text
        print("Please enter a value.")


def get_filter_date(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return date.fromisoformat(raw).isoformat()
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")


def get_operation(prompt, valid_options):
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print("Invalid choice. Please enter one of: " + ", ".join(valid_options))


def load_expenses():
    if not os.path.exists(CSV_FILE):
        return []
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except OSError:
        print(f"Warning: could not read {CSV_FILE}. Starting with an empty list.")
        return []


def save_expenses(expenses):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(expenses)


def print_table(expenses):
    print(f"\n{'Date':<12}{'Category':<14}{'Amount':>10}  {'Description'}")
    print("-" * 70)
    for e in expenses:
        amount = f"{float(e['Amount']):.2f}"
        print(f"{e['Date']:<12}{e['Category']:<14}{amount:>10}  {e['Description']}")
    print(f"\nEntries shown: {len(expenses)}")


def add_expense(expenses):
    print("\n--- Add Expense ---")
    category = get_category()
    amount = get_amount("Enter the amount spent: ")
    description = input("Short description (optional): ").strip()

    expense = {
        "Date": date.today().isoformat(),
        "Category": category,
        "Amount": f"{amount:.2f}",
        "Description": description,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Saved {category} expense of {amount:.2f} on {expense['Date']}. "
          f"(Total entries: {len(expenses)})")


def filter_expenses(expenses):
    print("\n--- Filter Expenses ---")
    choice = get_operation(
        "\n1. By category\n2. By date\n3. By minimum amount\nChoose an option (1-3): ",
        ["1", "2", "3"],
    )

    if choice == "1":
        category = get_filter_text("Filter by category: ")
        matches = [e for e in expenses if e["Category"] == category]
    elif choice == "2":
        day = get_filter_date("Filter by date (YYYY-MM-DD): ")
        matches = [e for e in expenses if e["Date"] == day]
    else:
        minimum = get_amount("Show entries with amount of at least: ")
        matches = [e for e in expenses if float(e["Amount"]) >= minimum]

    if not matches:
        print("\nNo entries matched this filter.")
    else:
        print_table(matches)


def show_summary(expenses):
    print("\n--- Category Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    counts = {}
    for e in expenses:
        category = e["Category"]
        totals[category] = totals.get(category, 0.0) + float(e["Amount"])
        counts[category] = counts.get(category, 0) + 1

    grand_total = sum(totals.values())

    print(f"\n{'Category':<14}{'Entries':>8}{'Total':>12}{'Share':>8}")
    print("-" * 44)
    for category in sorted(totals, key=totals.get, reverse=True):
        share = totals[category] / grand_total * 100
        print(f"{category:<14}{counts[category]:>8}{totals[category]:>12.2f}{share:>7.1f}%")
    print("-" * 44)
    print(f"{'GRAND TOTAL':<14}{len(expenses):>8}{grand_total:>12.2f}")

    top = max(totals, key=totals.get)
    print(f"\nYou spent the most on: {top} ({totals[top]:.2f})")


def main():
    print("=" * 40)
    print("     Personal Expense Tracker (CSV)")
    print("=" * 40)

    expenses = load_expenses()
    if expenses:
        print(f"Loaded {len(expenses)} existing entries from {CSV_FILE}.")
    else:
        print(f"No past records found. A new {CSV_FILE} will be created on your first entry.")

    while True:
        choice = get_operation(
            "\nMAIN MENU\n1. Add expense\n2. View all expenses\n3. Filter expenses\n"
            "4. Category summary\n5. Exit\nChoose an option (1-5): ",
            ["1", "2", "3", "4", "5"],
        )

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            if not expenses:
                print("\nNo expenses recorded yet.")
            else:
                print_table(expenses)
        elif choice == "3":
            filter_expenses(expenses)
        elif choice == "4":
            show_summary(expenses)
        else:
            print(f"All entries stay saved in {CSV_FILE}. Goodbye!")
            break


if __name__ == "__main__":
    main()


