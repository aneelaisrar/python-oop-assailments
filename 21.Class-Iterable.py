class Countdown:
    def __init__(self, start):
        self.start = start  # Set the start number

    # __iter__ method to return the iterator object
    def __iter__(self):
        self.current = self.start  # Initialize current value to start
        return self

    # __next__ method to return the next value in the countdown
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop the iteration once we reach 0
        self.current -= 1
        return self.current

# Create a Countdown object
countdown = Countdown(5)

# Use the Countdown object in a for-loop
for number in countdown:
    print(number)
