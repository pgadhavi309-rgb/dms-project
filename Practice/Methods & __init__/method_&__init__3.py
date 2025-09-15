class Laptop:
    def __init__(self, brand, ram = "8GB"):
        self.brand = brand
        self.ram = ram
    
    def details(self):
        print("Brand:", self.brand, "Ram:", self.ram)

l1 = Laptop("DELL", "16GB")
l2 = Laptop("HP")
l1.details()
l2.details()