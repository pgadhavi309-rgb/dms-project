class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    # Getter for balance
    def get_balance(self):
        return self.__balance


# Example
b1 = BankAccount(10000)
b1.deposit(5000)            # Adds 5000
b1.withdraw(3000)           # Subtracts 3000
print("Current balance:", b1.get_balance())  # 12000
