names = []

for _ in range(3):
    names.append(input("What name to add? "))

for name in sorted(names):
    print(f"Hello, {name}")

