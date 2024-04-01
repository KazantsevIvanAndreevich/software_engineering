class Person:
    def __init__(self, name, age):
        self._name = name  # Префикс _ указывает на защищенный атрибут
        self._age = age    # Префикс _ указывает на защищенный атрибут
    
    def greet(self):
        print(f"Привет, меня зовут {self._name} и мне {self._age} лет.")

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self._position = position  # Префикс _ указывает на защищенный атрибут
    
    def introduce(self):
        print(f"Привет, меня зовут {self._name}, мне {self._age} лет, и я работаю на должности {self._position}.")

# Создаем объект класса Employee
alice = Employee("Alice", 25, "менеджер")

# Попытка доступа к защищенным атрибутам напрямую вызовет ошибку
print(alice._name)        # Вызовет ошибку
print(alice._age)         # Вызовет ошибку
print(alice._position)    # Вызовет ошибку

# Однако мы можем использовать публичные методы классов для доступа к данным
alice.greet()             # Выведет: Привет, меня зовут Alice и мне 25 лет.
alice.introduce()         # Выведет: Привет, меня зовут Alice, мне 25 лет, и я работаю на должности менеджер.