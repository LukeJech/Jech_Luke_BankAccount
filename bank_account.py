import user

class BankAccount:
    bank_name = "Hero Bank"

    all_accounts = []
    
    def __init__(self, data, account_name = "savings"): 
        self.balance = data["initial_deposit"]
        self.int_rate = data["int_rate"]
        self.account_name = account_name
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You have ${self.balance} amount left in your {self.account_name} account")
        else: print("Insufficient funds")
        return self

    def display_account_info(self):
        print(f"Your {self.account_name} balance is ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def all_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()






