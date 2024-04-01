from datetime import datetime  # Импортируем класс datetime из модуля datetime

from math import sqrt  # Импортируем функцию sqrt (квадратный корень) из модуля math

def main(**kwargs):
    """
    Функция для вычисления квадратного корня суммы квадратов значений списка для каждой пары ключ-значение в переданных аргументах.

    Параметры:
    kwargs (dict): Словарь с произвольным количеством ключевых аргументов. Каждый ключ должен быть строкой, а значение - списком из двух чисел.

    Возвращаемое значение:
    None
    """
    for key in kwargs.items():  
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)  # Вычисляем квадратный корень суммы квадратов значений списка
        print(result)  # Выводим результат на экран

if __name__ == '__main__':  # Проверяем, запущен ли скрипт напрямую
    start_time = datetime.now()  # Записываем текущее время в переменную start_time
    
    main(  # Вызываем функцию main с передачей ей аргументов в виде словаря
        one=[10, 3],  # Передаем аргумент с ключом 'one' и значением [10, 3]
        two=[5, 4],   # Передаем аргумент с ключом 'two' и значением [5, 4]
        three=[15, 13],  # Передаем аргумент с ключом 'three' и значением [15, 13]
        four=[93, 53],   # Передаем аргумент с ключом 'four' и значением [93, 53]
        five=[133, 15]   # Передаем аргумент с ключом 'five' и значением [133, 15]
    )
    
    time_costs = datetime.now() - start_time  # Вычисляем время выполнения программы
    print(f"Время выполнения программы - {time_costs}")  # Выводим время выполнения на экран с помощью форматированной строки