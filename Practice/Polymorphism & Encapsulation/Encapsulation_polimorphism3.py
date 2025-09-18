class Student:
    def __init__(self, name, marks):
        self.name = name          # public variable
        self.__marks = marks      # private variable (double underscore se)

    # getter method
    def get_marks(self):
        return self.__marks

    # setter method
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

# Example
s1 = Student("Pragnesh", 85)
print(s1.name)        # direct access -> works
print(s1.get_marks()) # access private variable via getter
s1.set_marks(95)      # update marks via setter
print(s1.get_marks())
