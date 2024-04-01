# Создание собственного исключения
class MyCustomException(Exception):
    pass

# Функция, которая может вызвать исключение
def divide(a, b):
    if b == 0:
        raise MyCustomException("Деление на ноль недопустимо")
    return a / b

# Первый фрагмент кода, использующий собственное исключение
try:
    result = divide(10, 0)
except MyCustomException as e:
    print("Поймано собственное исключение:", e)

# Второй фрагмент кода, также использующий собственное исключение
try:
    x = int(input("Введите число: "))
    if x < 0:
        raise MyCustomException("Введено отрицательное число")
    else:
        print("Вы ввели положительное число")
except MyCustomException as e:
    print("Поймано собственное исключение:", e)