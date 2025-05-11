# Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")

# Department class with aggregation (Department contains Employee reference)
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Storing reference to an Employee object

    def show_department_details(self):
        print(f"Department: {self.department_name}")
        self.employee.show_details()  # Calling Employee's method through Department

# Creating an Employee object independently
employee1 = Employee("Anila", "Software Engineer")

# Creating a Department object that stores a reference to the Employee object
department1 = Department("IT", employee1)

# Displaying details
department1.show_department_details()

