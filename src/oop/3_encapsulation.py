# 4. Encapsulation
# Concept: Bundling data and methods, hiding internal state
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = max(initial_balance, 0)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Account Owner: {self.owner}. Current balance: ${self.__balance:.2f}")
        return self.__balance

account = BankAccount("Alice", 100)
account.get_balance()
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
