f = open("my_notes.txt", "w")
f.write("Hello, I am Pragnesh Raval.\n")
f.write("I learn Python file handling.\n")
f.write("I love Coding.\n")
f.close()

with open("my_notes.txt", "r") as f:
    for line in f:
        print(line, end="")
        