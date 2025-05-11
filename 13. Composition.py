# Engine class
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"{self.engine_type} engine is starting...")

# Car class using composition
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Engine object passed during initialization

    def start_car(self):
        print(f"{self.brand} car is ready to go!")
        self.engine.start()  # Accessing Engine's start method via Car

# Create Engine object
engine = Engine("V8")

# Create Car object and pass Engine object to it
car = Car("Toyota", engine)

# Start the car
car.start_car()
