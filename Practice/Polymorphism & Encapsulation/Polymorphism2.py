class Employee:
    def get_salary(self):
        print("Salary of employee")

class Developer(Employee):  # Developer inherits Employee
    def get_salary(self):
        print("Salary of developer")

# Objects
e = Employee()
d = Developer()

# Call methods
e.get_salary()  # Salary of employee
d.get_salary()  # Salary of developer
