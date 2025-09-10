def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
n = int(input("Enter number: "))
print(is_even(n))