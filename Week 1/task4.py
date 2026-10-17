
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money into the account
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            self.balance += amount
            print("Deposit successful!")

    # Withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawal successful!")

    # Display account details
    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


# Create a bank account object
account = BankAccount("Ayesha", 1000)

# Perform account operations
account.display_balance()

account.deposit(500)
account.display_balance()

account.withdraw(200)
account.display_balance()

account.withdraw(2000)
