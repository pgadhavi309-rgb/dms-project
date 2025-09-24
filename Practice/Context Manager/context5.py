class SafeDivide:
    def __enter__(self):
        return self  # self return karenge taaki division kar sake

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == ZeroDivisionError:
            print("Cannot divide by zero!")
            return True  # True return karne se exception handle ho jata hai
with SafeDivide() as sd:
    x = 10
    y = 0  # agar y = 0 hai to error ayega
    print("Result:", x / y)
