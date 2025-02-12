name = input("Enter a name: ")
file = open("names.txt", "w")
file.write(name)
file.close() 








"""
names = []

with open("names.txt") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} from {row[1]}") 




import csv

students = []

with open("names.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "house": row[1], "patronus": row[2]})

for student in students:
    print(f"{student['name']} from {student['house']} with {student['patronus']}")"""