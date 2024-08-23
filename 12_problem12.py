class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Function that accepts different objects
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Using polymorphism
rectangle = Rectangle(5, 10)
circle = Circle(7)

print_area(rectangle)  # Output: The area is: 50
print_area(circle)     # Output: The area is: 153.86
