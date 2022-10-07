class BankAccount:
    accounts = []
    
    def __init__(self, name:str, int_rate:int, balance:int):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit (self,amount):
        self.balance += amount
        return self
        
    def withdraw (self,amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            return self
        else:
            self.balance -= amount
            return self
        
    def display_account_info(self):
        print(f"{self.name}'s Balance: ${self.balance}")
        return self
        
    def yield_interest (self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self

    @classmethod
    def printinstances(cls):
        for account in cls.accounts:
            account.display_account_info()

account1 = BankAccount("First Account", 1.05, 300)
account2 = BankAccount("Second Account", 1.03, -300)

account1.deposit(50).deposit(100).deposit(3000).withdraw(60).yield_interest().display_account_info()
account2.deposit(500).deposit(300).withdraw(20).withdraw(100).withdraw(1).withdraw(20).yield_interest().display_account_info()

BankAccount.printinstances()
