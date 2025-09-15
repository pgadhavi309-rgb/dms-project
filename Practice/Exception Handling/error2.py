try:
    a = int(input("Enter number: "))
    
    if a < 1:
        print("Negative numner allowed nahi hai.")
    print("Square: ", a ** 2)
except ValueError:
    print("AApne number ki jagah kich aur likha hai.")

finally:
    print("Hello, Welcome sir!")