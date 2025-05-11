class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

    def bark(self):
        print(f"{self.name} is barking!")

# Create object of Dog
dog1 = Dog("Buddy", "Golden Retriever")

# Call the bark method
dog1.bark()
