class BankAccount:

    counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(amount, "transferred successfully")
        else:
            print("Insufficient balance")


# Creating two accounts
account1 = BankAccount("Khadija")
account2 = BankAccount("Ananya")

# Deposit
account1.deposit(5000)
account2.deposit(3000)

# Withdraw
account1.withdraw(1000)

# Transfer
account1.transfer(2000, account2)

# Display balances
account1.display_balance()
account2.display_balance()