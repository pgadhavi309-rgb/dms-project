class Account:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance( self):
        print(f"Balance: {self.__balance}")

    def diposite(self, ammount):
        if ammount > 0:
            self.__balance += ammount
            print(f{ammount} Diposited su)