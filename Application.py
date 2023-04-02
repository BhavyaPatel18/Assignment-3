class Program:
    def __init__(self):
        self.accounts = []

    def showMainMenu(self):
        while True:
            print("1. Open Account")
            print("2. Select Account")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                # Bonus implementation to open a new account
                print("Opening a new account...")
            elif choice == "2":
                account_number = input("Enter the account number: ")  
                account = self.findAccount(account_number)

                if account is not None:
                    self.showAccountMenu(account)
                else:
                    print("Account not found.")

            elif choice == "3":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def showAccountMenu(self, account):
        while True:
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            choice = input("Enter your choice: ")

            if choice == "1":
                balance = account.getBalance()
                print(f"Current balance: {balance}")
            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
                print("Deposit successful.")
            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                success = account.withdraw(amount)
                if success:
                    print("Withdrawal successful.")
                else:
                    print("Withdrawal failed. Insufficient balance.")
            elif choice == "4":
                print("Exiting account menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def findAccount(self, account_number):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                return account
        return None

    def run(self):
        self.showMainMenu()

application = Application()
application.run()