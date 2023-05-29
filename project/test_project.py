from project import BankAccount, create_account, deposit, withdraw, check_balance, financial_planning
from unittest.mock import patch

def test_create_account():
    account_holder = "John Doe"
    with patch('builtins.input', return_value=account_holder):
        account = create_account()
    assert isinstance(account, BankAccount)
    assert account.account_holder == account_holder
    assert account.balance == 0.0

def test_deposit(capsys):
    account = BankAccount("John Doe")
    with patch('builtins.input', return_value='100.0'):
        deposit(account)
    captured = capsys.readouterr()
    assert captured.out == "Deposit successful!\n"
    assert account.balance == 100.0

def test_withdraw(capsys):
    account = BankAccount("John Doe")
    with patch('builtins.input', return_value='50.0'):
        withdraw(account)
    captured = capsys.readouterr()
    assert captured.out == "Insufficient funds\n"
    assert account.balance == 0.0

def test_check_balance(capsys):
    account = BankAccount("John Doe")
    check_balance(account)
    captured = capsys.readouterr()
    assert captured.out == "Current balance: 0\n"

def financial_planning():
    goal_amount = float(input("Enter your financial goal amount: "))
    monthly_savings = float(input("Enter the amount you can save per month: "))

    months_to_goal = goal_amount / monthly_savings

    print(f"To reach your financial goal of {goal_amount:.2f}, you need to save {monthly_savings:.2f} per month.")
    print(f"It will take approximately {months_to_goal:.2f} months to reach your goal.")