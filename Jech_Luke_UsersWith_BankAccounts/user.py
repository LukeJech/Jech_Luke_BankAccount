import bank_account

class User:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["first_name"]
        self.email = data["email"]
        self.myaccounts = {
            "savings" : bank_account.BankAccount(data)
            }

    def make_deposit(self, amount, account_name):
        self.myaccounts[account_name].deposit(amount)

    def make_withdrawal(self, amount, account_name ):
        self.myaccounts[account_name].withdraw(amount)

    def display_user_balance(self,account_name):
        self.myaccounts[account_name].display_account_info()

    def add_account(self, account_name, data):
        self.myaccounts[account_name] = bank_account.BankAccount(data, account_name)

    def transfer_money(self, your_account_name, amount, other_user, other_user_account_name):
        print(f"Sending {amount} from your {your_account_name} account to {other_user.first_name}'s {other_user_account_name} account")
        self.make_withdrawal(amount, your_account_name)
        other_user.make_deposit(amount, other_user_account_name)
        
        
