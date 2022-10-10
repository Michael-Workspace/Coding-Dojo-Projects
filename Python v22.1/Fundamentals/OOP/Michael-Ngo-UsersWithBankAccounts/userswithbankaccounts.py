class BankAccount:
    accounts = []
    
    def __init__(self,balance:int=0, int_rate:int = 0.04):
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
        print(f"Account Balance: ${self.balance}")
        print("Interest Rate:", self.int_rate)
        return self
        
    def yield_interest (self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self

    @classmethod
    def printinstances(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    
    def __init__(self,name:str ="Unassigned", start_balance: int = 0, interest_rate: int = 0.04):
        self.name = name
        self.account = BankAccount(start_balance, interest_rate)
    
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self
    
michael = User("Michael Ngo")
michael.make_deposit(500).make_withdrawal(40).yield_interest().display_user_balance()

alexis = User("Alexis Miller")
alexis.make_deposit(1000).make_deposit(200).make_withdrawal(300).yield_interest().display_user_balance()