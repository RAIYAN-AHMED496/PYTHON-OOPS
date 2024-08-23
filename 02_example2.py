class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        print(f"Car: {self.brand} {self.model} {self.year}")


my_car = Car("Honda", "Civic", 2020)
my_car.get_info()

fathers_car = Car("lambo", "Farari", 2022)
fathers_car.get_info()
        
mother_car = Car("Haina", "Egle", 2021)
mother_car.get_info()