# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class of Person
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)


# Child class of Person
class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Working Hours:", self.working_hours)


# Multiple inheritance
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hours)
        print("Project Name:", self.project_name)


# Creating objects

person1 = Person("Rahul", 25)

employee1 = Employee("Anu", 28, "E101")

parttime1 = PartTime("Meera", 23, 20.5)

consultant1 = Consultant("Arjun", 30, "C101", 35.5, "Website Development")


# Displaying details

print("----- Person Details -----")
person1.show_details()

print("\n----- Employee Details -----")
employee1.show_details()

print("\n----- Part-Time Details -----")
parttime1.show_details()

print("\n----- Consultant Details -----")
consultant1.show_details()