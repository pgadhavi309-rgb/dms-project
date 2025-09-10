from utils import hash_password

user_password = input("Enter your password: ")
print("Hashed Password:", hash_password(user_password))



from utils import square, cube

print("Square of 5:", square(5))
print("Cube of 3:", cube(3))

test_utils.py

from utils import *

print("===== Math Helper Functions Test =====")
print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print("Factorial of 5:", factorial(5))
print("Square root of 16:", square_root(16))
print("2^3 =", power(2, 3))
print("Absolute value of -10:", absolute(-10))
print("Sine 30°:", sine(30))
print("Cosine 60°:", cosine(60))
print("Tangent 45°:", tangent(45))
print("Random integer between 1 and 10:", random_int(1, 10))

print("\n===== File Helper Functions Test =====")
file_name = "test_file.txt"

# Create
create_file(file_name, "Hello World!\n")

# Read
print("File content after create:")
print(read_file(file_name))

# Append
append_file(file_name, "Ye ek aur line add ho gayi!\n")
print("File content after append:")
print(read_file(file_name))

# Write (overwrite)
write_file(file_name, "Ye purana content replace kar diya.\n")
print("File content after write:")
print(read_file(file_name))

# Delete
delete_file(file_name)
print("File content after delete (should give message):")
print(read_file(file_name))
