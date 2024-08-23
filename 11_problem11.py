class Student:
    def __init__(self, name, grade=0):
        self.name = name
        self.__grade = grade  # Private attribute

    def update_grade(self, number):
        self.__grade += number
        print(f"Grade updated. New grade: {self.__grade}")

    def decrease_grade(self, amount):
        if self.__grade > 20:
            self.__grade -= amount
            print(f"Grade decreased. New grade: {self.__grade}")
        else:
            print("Grade cannot be decreased below 20.")

    def get_grade(self):
        return self.__grade

# Example usage
Raiyan = Student("Raiyan", 100)
print(Raiyan.get_grade())  # Output: 100

Raiyan.update_grade(10)    # Output: Grade updated. New grade: 110
Raiyan.decrease_grade(30)  # Output: Grade decreased. New grade: 80
Raiyan.decrease_grade(70)  # Output: Grade decreased. New grade: 10

