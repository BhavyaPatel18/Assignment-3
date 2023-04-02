import Account

class ChequingAccount(Account):
    def __init__(self, acc_num, balance, overdraft_limit):
        super().__init__(acc_num, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            super().withdraw(amount)
        else:
            print("Transaction not permitted. Overdraft limit exceeded.")
            
a = ChequingAccount()
print(a.balance)