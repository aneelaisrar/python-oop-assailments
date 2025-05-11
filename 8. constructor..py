# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject

    def show_details(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Creating object
t1 = Teacher("Anila", "Mathematics")

# Displaying details
t1.show_details()
