try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result: ", a / b)

except ZeroDivisionError:
    print("Zero se devide nahi kar sakte")
except ValueError:
    print("Aapne number ki jagah kuch aur likha hai")
finally:
    print("Welcome sir!")