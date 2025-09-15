try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)   # yaha error aa sakta hai

except ValueError:
    print("Aapne number ki jagah kuch aur likha hai.")
except ZeroDivisionError:
    print("Zero se divide nahi kar sakte!")
finally:
    print("Operation successful 💕")
