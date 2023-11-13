import json
from datetime import datetime

class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Budget:
    def __init__(self, month, year, income):
        self.month = month
        self.year = year
        self.income = income
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_remaining_budget(self):
        return self.income - self.get_total_expenses()

def main():
    print("Welcome to your Monthly Budget Tracker!")

    month = input("Enter the current month: ")
    year = int(input("Enter the current year: "))
    income = float(input("Enter your monthly income: "))

    budget = Budget(month, year, income)

    while True:
        print("\n1. Add an Expense")
        print("2. View Expenses")
        print("3. View Budget Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense(budget)
        elif choice == '2':
            view_expenses(budget)
        elif choice == '3':
            view_budget_summary(budget)
        elif choice == '4':
            save_budget(budget)
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_expense(budget):
    description = input("Enter the expense description: ")
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")

    expense = Expense(description, amount, category)
    budget.add_expense(expense)

    print("Expense added successfully!")

def view_expenses(budget):
    print("\n--- Your Expenses ---")
    for expense in budget.expenses:
        print(f"{expense.description} - RS{expense.amount} on {expense.date}")

def view_budget_summary(budget):
    total_expenses = budget.get_total_expenses()
    remaining_budget = budget.get_remaining_budget()

    print(f"\n--- Budget Summary ---")
    print(f"Total Income: RS{budget.income}")
    print(f"Total Expenses: RS{total_expenses}")
    print(f"Remaining Budget: RS{remaining_budget}")

def save_budget(budget):
    filename = f"budget_{budget.month.lower()}_{budget.year}.json"
    with open(filename, 'w') as file:
        data = {
            "month": budget.month,
            "year": budget.year,
            "income": budget.income,
            "expenses": [{"description": e.description, "amount": e.amount, "category": e.category, "date": e.date} for e in budget.expenses]
        }
        json.dump(data, file)

if __name__ == "__main__":
    main()
