def remove_first_occurrence(tup, element):
    # Проверяем наличие элемента в кортеже
    if element in tup:
        # Находим индекс первого появления элемента
        index = tup.index(element)
        # Преобразуем кортеж в список для удаления элемента
        lst = list(tup)
        # Удаляем элемент из списка
        lst.pop(index)
        # Преобразуем список обратно в кортеж
        return tuple(lst)
    else:
        # Если элемент не найден, возвращаем исходный кортеж
        return tup

# Тестовые данные
data = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9)
]

# Проверяем функцию для каждого тестового случая
for tup, elem in data:
    result = remove_first_occurrence(tup, elem)
    print(result)