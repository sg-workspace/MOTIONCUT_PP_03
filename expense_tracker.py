import json

FILENAME = "expenses.json"

def load_expenses():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file)

def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    name = input("Enter the name of the expense: ")
    amount = float(input("Enter the amount: "))
    expense = {"date": date, "name": name, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added for {name} on {date} with amount ${amount:.2f}.")

def view_expenses(expenses):
    for expense in expenses:
        print(f"Date: {expense['date']}, Name: {expense['name']}, Amount: ${expense['amount']:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
