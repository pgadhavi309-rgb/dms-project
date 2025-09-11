import csv
with open("book.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Author", "Price"])
    writer.writerow(["Pyhon Basic", "John", 250])
    writer.writerow(["Learning AI", "Alice", 350])
    writer.writerow(["DAta science", "Bob", 300])

print("CSV file created and data written!")

with open("book.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Machine learning", "Eve", 400])

with open("book.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)