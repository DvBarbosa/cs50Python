class BankAccount:
    def __init__(self, account_holder):
        self.balance = 0
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount

    def check_balance(self):
        return self.balance


def create_account():
    account_holder = input("Enter your name: ")
    account = BankAccount(account_holder)
    print("Account created successfully!")
    return account


def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account.deposit(amount)
    print("Deposit successful!")


def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    result = account.withdraw(amount)
    if result == "Insufficient funds":
        print(result)
    else:
        print("Withdrawal successful!")


def check_balance(account):
    balance = account.check_balance()
    print(f"Current balance: {balance}")
    return balance


def financial_planning():
    goal_amount = float(input("Enter your financial goal amount: "))
    monthly_savings = float(input("Enter the amount you can save per month: "))

    months_to_goal = goal_amount / monthly_savings

    print(f"To reach your financial goal of {goal_amount}, you need to save {monthly_savings} per month.")
    print(f"It will take approximately {months_to_goal:.2f} months to reach your goal.")


def main():
    account = None
    while True:
        print("Bank Account Menu:")
        print("1 - Create account")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Check balance")
        print("5 - Financial planning")
        print("6 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account = create_account()
        elif choice == "2":
            if not account:
                print("You must create an account first")
            else:
                deposit(account)
        elif choice == "3":
            if not account:
                print("You must create an account first")
            else:
                withdraw(account)
        elif choice == "4":
            if not account:
                print("You must create an account first")
            else:
                check_balance(account)
        elif choice == "5":
            financial_planning()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
