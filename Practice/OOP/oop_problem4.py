class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def show_specs(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB")
    
    def upgrade_ram(self, extra_ram):
        self.ram += extra_ram
        print(f"RAM upgraded to {self.ram}GB")

my_laptop = Laptop("HP", 12)
my_laptop.show_specs()
my_laptop.upgrade_ram(6)
my_laptop.show_specs()