class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Creating objects of Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} says: {dog.sound()}")  # Output: Buddy says: Woof!
print(f"{cat.name} says: {cat.sound()}")  # Output: Whiskers says: Meow!
