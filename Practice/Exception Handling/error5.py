numbers = [2, 4, "abc", 7, 10]

try:
    for n in numbers:
        print("Square:", n ** 2)
except TypeError:
    print("Error: Non-numeric value found in list!")
except ValueError:
    print("Error: Invalid value in list!")
else:
    print("All elements processed successfully 💕")
finally:
    print("Program finished 😘")
