n = int(input("How many students name they want to add "));
try:
    with open("students.txt", "r") as file:
        existing_names = file.read()

    print("\nExisting student names:")
    print(existing_names)
except FileNotFoundError:
    print("\nNo existing student file found.")
    with open("students.txt", "a") as file:
     for i in range(n):
        name = input(f"Enter student name {i + 1}: ")
        file.write(name + "\n")
    print("\nUpdated list of student names:")
with open("students.txt", "r") as file:
    for name in file:
        print(name.strip())