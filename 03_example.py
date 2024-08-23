# Defining a class named 'Car'
class Car:
    def __init__(self, brand, model, year, mileage=0): # it initializes the object's attribute when an object is created
        self.brand = brand  # Attribute
        self.model = model  # Attribute
        self.year = year    # Attribute
        self.mileage = mileage

    def get_info(self):
        print(f"Car: {self.brand} {self.model} {self.year} - {self.mileage} Km.")

    def drive(self, distance):
        self.mileage += distance
        print(f"Driven {distance} Km. Total mileage is now {self.mileage} Km.")

# Creating an object of the Car class
my_car = Car("Honda", "Civic", 2023)

# Accessing the methods
my_car.get_info()    # Output: Car: Honda Civic 2023 - 0 Km.
my_car.drive(500)    # Output: Driven 500 Km. Total mileage is now 500 Km.
my_car.drive(490)    # Output: Driven 490 Km. Total mileage is now 990 Km.
my_car.drive(10)     # Output: Driven 10 Km. Total mileage is now 1000 Km.
