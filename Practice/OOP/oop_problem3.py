class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self, distance):
        print(f"{self.brand}, is driving {distance} km")

my_car = car("Bugati", "black")
my_car.drive(100)
