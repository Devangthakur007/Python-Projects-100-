import sys
import random

class BankAccount:
    """Class representing an individual bank account."""
    def __init__(self, name: str, initial_deposit: float = 0.0):
        self.name = name
        # Generate a random 6-digit account number
        self.account_number = str(random.randint(100000, 999999))
        self.balance = initial_deposit
        self.transaction_history = []
        
        # Log opening deposit
        if initial_deposit > 0:
            self.transaction_history.append(f"Initial Deposit: +${initial_deposit:.2f}")

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print(" Deposit amount must be positive.")
            return False
        self.balance += amount
        self.transaction_history.append(f"Deposited: +${amount:.2f}")
        print(f" Successfully deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print(" Insufficient funds!")
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: -${amount:.2f}")
        print(f" Successfully withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
        return True

    def display_statement(self):
        print(f"\n--- Statement for Account #{self.account_number} ({self.name}) ---")
        print(f"Current Balance: ${self.balance:.2f}")
        print("Transaction History:")
        if not self.transaction_history:
            print("  No transactions yet.")
        else:
            for item in self.transaction_history:
                print(f"  • {item}")
        print("-" * 45)


class BankSystem:
    """Class managing all accounts in the bank."""
    def __init__(self):
        self.accounts = {}  # Stores account_number -> BankAccount object

    def create_account(self, name: str, initial_deposit: float) -> BankAccount:
        new_account = BankAccount(name, initial_deposit)
        self.accounts[new_account.account_number] = new_account
        print(f"\n Account created successfully!")
        print(f"Account Holder: {name}")
        print(f"Account Number: {new_account.account_number}")
        print(f"Starting Balance: ${initial_deposit:.2f}\n")
        return new_account

    def get_account(self, account_number: str) -> BankAccount:
        return self.accounts.get(account_number)


def get_float_input(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt).strip())
            if val < 0:
                print(" Please enter a non-negative number.")
                continue
            return val
        except ValueError:
            print(" Invalid input! Please enter a valid number.")


def main():
    bank = BankSystem()
    print("=== Python Basic Banking System ===")

    while True:
        print("\nMain Menu:")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance / Mini Statement")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '5':
            print("Thank you for using Python Bank. Goodbye!")
            sys.exit()

        elif choice == '1':
            name = input("Enter account holder name: ").strip()
            if not name:
                print(" Name cannot be empty!")
                continue
            deposit = get_float_input("Enter initial deposit amount: $")
            bank.create_account(name, deposit)

        elif choice in ['2', '3', '4']:
            acc_num = input("Enter your 6-digit Account Number: ").strip()
            account = bank.get_account(acc_num)

            if not account:
                print(" Account not found! Please check the account number.")
                continue

            if choice == '2':
                amount = get_float_input("Enter deposit amount: $")
                account.deposit(amount)

            elif choice == '3':
                amount = get_float_input("Enter withdrawal amount: $")
                account.withdraw(amount)

            elif choice == '4':
                account.display_statement()

        else:
            print(" Invalid option! Please select from 1 to 5.")


if __name__ == "__main__":
    main()