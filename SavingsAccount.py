import Account

class SavingsAccount(Account):
    def __init__(self, acc_num, balance, min_balance):
        super().__init__(acc_num, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            super().withdraw(amount)
        else:
            print("Transaction not permitted. Minimum balance must be maintained.")
            
a = SavingsAccount()
print(a.balance)