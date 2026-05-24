class bankacc:
    def __init__(self,bal,owner):
        self.bal = bal
        self.owner = owner
    
    def deposit(self,amount):
        self.amount = amount
        self.bal = self.bal+self.amount
        print("your current balance = ",self.bal)
    def withdraw(self,amount):
        self.amount = amount
        if(self.bal >= self.amount):
            self.bal = self.bal-self.amount
        else:
            print("insufficient balance") 
        print("your current balance = ",self.bal)      

class savingsacc(bankacc):
    def __init__(self,bal,owner,interest_rate):
        super().__init__(bal,owner)
        self.interest_rate = interest_rate
    
    def apply_interest(self,interest):
        self.interest = interest
        credit = (self.interest/100) * self.bal 
        self.bal = self.bal +credit
        print(credit)
s1 = savingsacc(5000, "John", 4)
s1.apply_interest(5)
print(s1.bal)
s1.deposit(100)