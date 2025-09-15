try:
    file = open(input("Enter file name: "), "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File does not exist.")
except:
    print("Kuch galat ho gaya!")
finally:
    try:
        file.close()
    except:
        pass
    print("File operation completed 💕")
