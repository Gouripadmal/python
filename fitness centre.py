class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)


class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)


# Creating objects

employee1 = Employee("Rahul", "Manager")

trainer1 = Trainer("Arun", "Trainer", "Strength Training")

yoga1 = YogaInstructor("Meera", "Yoga Instructor", "Hatha Yoga")

multi1 = MultiTrainer(
    "Anjali",
    "Multi Trainer",
    "Weight Training",
    "Vinyasa Yoga"
)


# Displaying details

print("----- Employee -----")
employee1.display()

print("\n----- Trainer -----")
trainer1.display()

print("\n----- Yoga Instructor -----")
yoga1.display()

print("\n----- Multi Trainer -----")
multi1.display()