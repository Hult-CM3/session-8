# this is a comment
""" 
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close() """

""" names = []

with open("names.txt") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} from {house}") """

import csv

students = []

with open("names.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "house": row[1], "patronus": row[2]})

for student in students:
    print(f"{student['name']} from {student['house']} with {student['patronus']}")