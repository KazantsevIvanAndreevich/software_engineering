import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Функция, которая принимает любой объект Shape и вызывает его метод area()
def print_area(shape):
    print("Area:", shape.area())

# Создаем экземпляры классов
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Вызываем функцию print_area() с разными объектами Shape
print_area(rectangle)  # Вывод: Area: 15
print_area(circle)     # Вывод: Area: 50.26548245743669