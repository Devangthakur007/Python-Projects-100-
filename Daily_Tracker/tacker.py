import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    amount = float(input("Enter amount ($): "))
    category = input("Enter category (e.g., Food, Transport, Rent): ").strip()
    description = input("Enter description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("\n✅ Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses logged yet.")
        return

    print("\n--- Expense History ---")
    total = 0
    for idx, item in enumerate(expenses, 1):
        print(f"{idx}. [{item['date']}] {item['category']} - ${item['amount']:.2f} ({item['description']})")
        total += item['amount']
    
    print("-" * 25)
    print(f"Total Spent: ${total:.2f}\n")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses & Total")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()