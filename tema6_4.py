def extract_employee_log(log, id):
    # Ищем первое вхождение элемента id в кортеже
    first_occurrence = log.index(id) if id in log else -1

    # Если элемента нет в кортеже, возвращаем пустой кортеж
    if first_occurrence == -1:
        return ()

    # Ищем второе вхождение элемента id в кортеже, начиная с индекса first_occurrence + 1
    second_occurrence = log.index(id, first_occurrence + 1) if id in log[first_occurrence + 1:] else -1

    # Если элемент встречается только один раз, возвращаем часть кортежа, начиная с него
    if second_occurrence == -1:
        return log[first_occurrence:]

    # Возвращаем часть кортежа, начиная с первого вхождения id и заканчивая вторым включительно
    return log[first_occurrence:second_occurrence + 1]

# Примеры использования функции
logs = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

for log, id in logs:
    result = extract_employee_log(log, id)
    print(result)