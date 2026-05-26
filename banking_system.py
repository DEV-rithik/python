import csv
import os

class bankacc:
    def __init__(self, bal, owner):
        self.bal = bal
        self.owner = owner
    
    def deposit(self, amount):
        self.amount = amount
        self.bal = self.bal + self.amount
        print("Your current balance = ", self.bal)
    
    def withdraw(self, amount):
        self.amount = amount
        if(self.bal >= self.amount):
            self.bal = self.bal - self.amount
        else:
            print("Insufficient balance") 
        print("Your current balance = ", self.bal)
    
    def save_to_file(self):
        file_exists = os.path.isfile("meow.csv")
        with open("meow.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Owner", "Balance"])
            writer.writerow([self.owner, self.bal])
        print("Data saved to meow.csv")


class savingsacc(bankacc):
    def __init__(self, bal, owner, interest_rate):
        super().__init__(bal, owner)
        self.interest_rate = interest_rate
    
    def apply_interest(self, interest):
        self.interest = interest
        credit = (self.interest / 100) * self.bal 
        self.bal = self.bal + credit
        print(f"Interest credited: {credit}")


def main():
    print("===== Banking System =====\n")
    
    # Get user input
    owner_name = input("Enter account owner name: ")
    initial_balance = float(input("Enter initial balance: "))
    account_type = input("Is this a savings account? (yes/no): ").lower()
    
    # Create account based on type
    if account_type == "yes":
        interest_rate = float(input("Enter interest rate: "))
        account = savingsacc(initial_balance, owner_name, interest_rate)
    else:
        account = bankacc(initial_balance, owner_name)
    
    # Menu
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Save & Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current balance: {account.bal}")
        elif choice == "4":
            account.save_to_file()
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
