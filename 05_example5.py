class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"The name of the person is {self.name} and his/her age is {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) 
        self.student_id = student_id
    def show_info_of_student(self):
        print(f"The name of the student is {self.name} age: {self.age} id: {self.student_id}")


raiyan = Student("Raiyan", 17, 518189)
raiyan.show_info_of_student()
        
harry = Person("Harry", 35)
harry.show_info()

harry = Student("Harry", 35, 41414)
harry.show_info_of_student()