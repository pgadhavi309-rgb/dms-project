import csv
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Department", "Salary"])
    writer.writerow(["Pragnesh", "IT", 100000])
    writer.writerow(["Parth", "HR", 50000])
    writer.writerow(["Himu", "AI", 90000])

print("CSV file created and data written!")

with open("employees.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Yash", "Manager", 80000])

with open("employees.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)