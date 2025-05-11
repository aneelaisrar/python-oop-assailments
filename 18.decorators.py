class Product:
    def __init__(self, price):
        self._price = price  # Private attribute _price

    # @property decorator to get the price
    @property
    def price(self):
        return self._price

    # @price.setter decorator to set the price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    # @price.deleter decorator to delete the price
    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Create a product object
product = Product(100)

# Access price using the getter
print(f"Product price: {product.price}")

# Update price using the setter
product.price = 150
print(f"Updated product price: {product.price}")

# Try setting a negative price
product.price = -50

# Delete the price using the deleter
del product.price
