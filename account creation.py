from abc import ABC, abstractmethod
# Abstract base class
class User(ABC):

    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    # Concrete method
    def account_age(self):
        return 2025 - self.account_year

    # Abstract method
    @abstractmethod
    def get_role(self):
        pass


# Admin subclass
class Admin(User):

    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"Admin User: {self.name}"


# Guest subclass
class Guest(User):

    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"Guest User: {self.name}"


# Creating objects
admin = Admin("Alice", 2020)
guest = Guest("Bob", 2023)

# Printing details
print(admin.get_role())
print(admin.account_age())
print(admin)

print(guest.get_role())
print(guest.account_age())
print(guest)