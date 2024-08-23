class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f"The car manufacturing company {self.make} made the model {self.model} in {self.year}.")

# Creating an instance of Car
my_car = Car("Toyota", "Suzuki", 2022)
my_car.start_engine()  # Output: The car manufacturing company Toyota made the model Suzuki in 2022.
