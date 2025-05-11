class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (by convention)
        self.__ssn = ssn        # Private variable (name mangling)

# Create an object
emp = Employee("Anila", 50000, "123-45-6789")

# Accessing public variable
print("Name:", emp.name)

# Accessing protected variable (possible, but not recommended outside the class)
print("Salary:", emp._salary)

# Accessing private variable (will raise error)
try:
    print("SSN:", emp.__ssn)  # ❌ This will raise AttributeError
except AttributeError as e:
    print("Error accessing __ssn:", e)

# Accessing private variable using name mangling (not recommended, but possible)
print("SSN via name mangling:", emp._Employee__ssn)
