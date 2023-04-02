class Account:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.acc_num

class Bank:
    def __init__(self, SavingsAccount, ChequingAccount):
        self.accounts = [
            SavingsAccount("SA001", 10000, 5000),
            ChequingAccount("CH001", 5000, 5000),
            SavingsAccount("SA002", 20000, 7000),
            ChequingAccount("CH002", 10000, 10000),
            SavingsAccount("SA003", 15000, 6000)
        ]

    def searchAccount(self, acc_num):
        for acc in self.accounts:
            if acc.get_account_number() == acc_num:
                return acc
        return None

    def openAccount(self, acc_type, acc_num, balance, min_balance=None, overdraft_limit=None):
        if acc_type == "SA":
            acc = SavingsAccount(acc_num, balance, min_balance)
        elif acc_type == "CH":
            acc = ChequingAccount(acc_num, balance, overdraft_limit)
        else:
            print("Invalid account type.")
            return

        self.accounts.append(acc)
        print(f"Account {acc_num} opened successfully.")
        
a = Account(123, 4000)
print(a.balance)
