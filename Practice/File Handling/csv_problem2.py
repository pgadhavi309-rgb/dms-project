import csv
with open("student.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Pragnesh", 22, 95])
    writer.writerow(["Himu", 20, 90])
    writer.writerow(["Himani", 22, 33])

print("CSV file created and data written!")

with open("student.csv", "r") as f:
    for line in f:
        print(line, end="")