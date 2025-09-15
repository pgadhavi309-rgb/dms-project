def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

n = int(input("Enter number: "))
print(is_prime(n))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Use
print("Is Prime:", is_prime(17))
print("Is Prime:", is_prime(18))
