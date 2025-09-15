class Student:
    def __init__(self, name, age):  # name aur age parameters
        self.name = name  # object ke liye assign kar rahe hain
        self.age = age

    def greet(self):  # method
        print(f"Hello, I am {self.name}, and I am {self.age} years old")

# Object create karte hain
my_name = Student("Pragnesh", 22)
my_name.greet()  # Hello, I am Pragnesh, and I am 22 years old

friend = Student("Chirag", 18)
friend.greet()  # Hello, I am Chirag, and I am 18 years old
