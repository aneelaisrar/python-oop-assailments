class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):
        print(f"The {self.brand} car is starting...")  # Public method

# Instantiate the class
my_car = Car("Toyota")

# Accessing public variable and method from outside the class
print("Car Brand:", my_car.brand)
my_car.start()
