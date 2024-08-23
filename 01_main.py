# Defining a class named 'Car'
class Car:
    def __init__(self, brand, model, year): # it initializes the object's attribute when an object is created
        self.brand = brand  # Attribute
        self.model = model  # Attribute
        self.year = year    # Attribute

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing the attributes
print(my_car.brand)  # Output: Toyota

# Calling a method
my_car.display_info()  # Output: Car: Toyota Corolla (2020)
