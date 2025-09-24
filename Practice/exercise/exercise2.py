def calculate_total(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Function call
total = calculate_total(10, 20, 30)
print(total)
