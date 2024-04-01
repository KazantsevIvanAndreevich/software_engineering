# Получаем данные от пользователя
data = input("Введите последовательность чисел, разделенных пробелом: ")

# Разделяем строку на числа и преобразуем их в список
number_list = list(map(int, data.split()))

# Преобразуем список в кортеж
number_tuple = tuple(number_list)

# Выводим результат
print("Список:", number_list)
print("Кортеж:", number_tuple)