python_students = {"Anu", "Rahul", "Arun"}
data_science_students = {"Rahul", "Meera", "Arun"}

python_students.add("Neha")
data_science_students.remove("Meera")

both_courses = python_students.intersection(data_science_students)
print("Students in both courses:", both_courses)

python_only = python_students.difference(data_science_students)
print("Students only in Python:", python_only)

all_students = python_students.union(data_science_students)
print("All students:", all_students)

courses = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, students in courses.items():
    print(f"Course: {course}, Students: {students}")

expected_growth = {
    course: students * 2
    for course, students in courses.items()
}

print("Expected growth:", expected_growth)