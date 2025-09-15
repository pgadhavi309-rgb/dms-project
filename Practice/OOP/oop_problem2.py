class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def greet(self):
        print(f"{self.name}, is barking.")

my_dog = dog("Tommy", "Bull")
my_dog.greet()


