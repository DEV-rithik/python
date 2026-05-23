class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✓ Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("✗ Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"✓ Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print(f"✗ Insufficient balance. Available: ${self.balance}")
        else:
            print("✗ Withdrawal amount must be positive.")
    
    def check_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")
    
    def __str__(self):
        return f"{self.account_holder} - Account: {self.account_number} - Balance: ${self.balance}"


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}
    
    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number in self.accounts:
            print(f"✗ Account {account_number} already exists.")
            return False
        
        self.accounts[account_number] = BankAccount(account_number, account_holder, initial_balance)
        print(f"✓ Account created successfully for {account_holder}")
        return True
    
    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"✗ Account {account_number} not found.")
            return None
    
    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        
        print(f"\n{self.bank_name} - All Accounts:")
        for account in self.accounts.values():
            print(account)


def main():
    print("=" * 50)
    print("Welcome to Simple Banking System")
    print("=" * 50)
    
    bank = Bank("Python Bank")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View All Accounts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            account_num = input("Enter account number: ").strip()
            name = input("Enter account holder name: ").strip()
            try:
                initial = float(input("Enter initial balance (optional, press 0 for none): ").strip())
                bank.create_account(account_num, name, initial)
            except ValueError:
                print("✗ Invalid amount. Please enter a number.")
        
        elif choice == '2':
            account_num = input("Enter account number: ").strip()
            account = bank.get_account(account_num)
            if account:
                try:
                    amount = float(input("Enter deposit amount: ").strip())
                    account.deposit(amount)
                except ValueError:
                    print("✗ Invalid amount. Please enter a number.")
        
        elif choice == '3':
            account_num = input("Enter account number: ").strip()
            account = bank.get_account(account_num)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: ").strip())
                    account.withdraw(amount)
                except ValueError:
                    print("✗ Invalid amount. Please enter a number.")
        
        elif choice == '4':
            account_num = input("Enter account number: ").strip()
            account = bank.get_account(account_num)
            if account:
                print()
                account.check_balance()
        
        elif choice == '5':
            bank.display_all_accounts()
        
        elif choice == '6':
            print("Thank you for using Python Bank. Goodbye!")
            break
        
        else:
            print("✗ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
