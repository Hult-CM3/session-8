name = input("What name to add? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()