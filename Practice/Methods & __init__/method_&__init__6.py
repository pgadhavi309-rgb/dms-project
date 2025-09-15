class Wallet:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def add_money(self, ammount):
        self.balance += ammount
        print(f"Diposited {ammount}. New balance: {self.balance}")

    def spend_money(self, ammount):
        if ammount > self.balance:
            print("Not enough money")
        else:
            self.balance -= ammount
            print(f"spend_money {ammount}. New balance: {self.balance}")
    def show_balance(self):
        print(f"Account holder: {self.owner},  Balance: {self.balance}")

a1 = Wallet("Pragnesh")
a1.show_balance()

a1.add_money(10000)
a1.spend_money(6000)
a1.spend_money(6000)
