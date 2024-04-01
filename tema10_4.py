def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("До выполнения функции")
        result = func(*args, **kwargs)
        print("После выполнения функции")
        return result
    return wrapper

# Функция, которая будет использовать декоратор
@my_decorator
def greet(name):
    print("Привет, {}!".format(name))

# Еще одна функция с использованием декоратора
@my_decorator
def square(x):
    return x * x

# Вызов функций
greet("Вовочка")
print("Результат возведения в квадрат:", square(5))