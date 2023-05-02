class BankAccount:
    bank_name = "Hero Bank"

    all_accounts = []
    
    def __init__(self, int_rate, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You have ${self.balance} amount left in your account")
        else: print("Insufficient funds")
        return self

    def display_account_info(self):
        print(f"Your balance is ${self.balance}")
        print(f"Your interest rate is {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def all_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()


luke_data= {
    "first_name": "Luke",
    "last_name": "Jech",
    "balance" : 100,
    "int_rate" : .03
}
steve_data= {
    "first_name": "Steve",
    "last_name": "Rogers",
    "balance" : 569645,
    "int_rate" : .09
}

luke_account = BankAccount(luke_data["int_rate"], luke_data["balance"])
steve_account = BankAccount(steve_data["int_rate"], steve_data["balance"])

luke_account.deposit(50).deposit(500).deposit(100).withdraw(700).yield_interest().display_account_info()

steve_account.deposit(693).deposit(420000).withdraw(20).withdraw(40).withdraw(60).withdraw(80).yield_interest().display_account_info()

BankAccount.all_info()