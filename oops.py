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
    def __init__(self,interest_rate):
        self.interest_rate = interest_rate
    
    