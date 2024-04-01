class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
    
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, и я работаю на должности {self.position}.")

# Создаем объект класса Employee
alice = Employee("Alice", 25, "менеджер")

# Вызываем метод greet из класса Person
alice.greet()

# Вызываем метод introduce из класса Employee
alice.introduce()