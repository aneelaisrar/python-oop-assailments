# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    else:
        print("Age is valid.")

# Test the function with try...except
try:
    age = int(input("Enter your age: "))  # Taking age input from user
    check_age(age)
except InvalidAgeError as e:
    print(f"Invalid Age Error: {e}")
except ValueError:
    print("Please enter a valid number for age.")
