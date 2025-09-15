class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name, "Age:", self.age)

s1 = Student("Pragnesh", 22)
s1.show()

s2 = Student("Parth", 22)
s2.show()