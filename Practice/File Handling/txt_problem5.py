f = open("data.txt", "w")
f.write("Python is fun\n")
f.write("I enjoy coding\n")
f.write("Himu is my best teacher\n")
f.close()

f = open("data.txt", "a")
f.write("Learning never stop\n")
f.close()

f = open("data.txt", "r")
content = f.readlines()
print(content)