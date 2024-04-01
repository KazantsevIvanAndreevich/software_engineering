class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")

# Создаем объект класса Person
john = Person("John", 30)

# Вызываем метод greet для объекта john
john.greet()