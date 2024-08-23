class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"The {self.name} says {self.sound}")

class Bird(Animal):
    def fly(self):
        print(f"The {self.name} is flying high in the sky!")

# Creating an instance of Bird
my_bird = Bird("Parrot", "Squawk")
my_bird.speak()  # Output: The Parrot says Squawk
my_bird.fly()    # Output: The Parrot is flying high in the sky!
