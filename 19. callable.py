class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the factor during initialization

    def __call__(self, value):
        return value * self.factor  # Multiply input value by the factor

# Create an instance of Multiplier with a factor of 5
multiplier = Multiplier(5)

# Test if the object is callable
print(callable(multiplier))  # Output: True

# Use the object like a function
result = multiplier(10)  # This will multiply 10 by the factor 5
print(f"Result: {result}")
