import json
from project import Expense, Budget, add_expense, view_expenses, view_budget_summary, save_budget

def test_add_expense():
    budget = Budget("January", 2023, 5000.0)
    initial_expense_count = len(budget.expenses)

    add_expense(budget)

    assert len(budget.expenses) == initial_expense_count + 1

def test_view_expenses(capfd):
    budget = Budget("January", 2023, 5000.0)
    expense1 = Expense("Groceries", 150.0, "Food")
    expense2 = Expense("Internet Bill", 50.0, "Utilities")
    budget.expenses = [expense1, expense2]

    view_expenses(budget)

    captured = capfd.readouterr()
    assert "Groceries" in captured.out
    assert "Internet Bill" in captured.out

def test_view_budget_summary(capfd):
    budget = Budget("January", 2023, 5000.0)
    expense1 = Expense("Groceries", 150.0, "Food")
    expense2 = Expense("Internet Bill", 50.0, "Utilities")
    budget.expenses = [expense1, expense2]

    view_budget_summary(budget)

    captured = capfd.readouterr()
    assert "Total Income: $5000.0" in captured.out
    assert "Total Expenses: $200.0" in captured.out
    assert "Remaining Budget: $4800.0" in captured.out

def test_save_budget(tmp_path):
    budget = Budget("January", 2023, 5000.0)
    expense1 = Expense("Groceries", 150.0, "Food")
    expense2 = Expense("Internet Bill", 50.0, "Utilities")
    budget.expenses = [expense1, expense2]

    file_path = tmp_path / "test_budget.json"
    save_budget(budget, file_path)

    with open(file_path, 'r') as file:
        data = json.load(file)

    assert data["month"] == budget.month
    assert data["year"] == budget.year
    assert data["income"] == budget.income
    assert len(data["expenses"]) == len(budget.expenses)
