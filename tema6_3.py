def count_digits(s):
    # Создаем словарь для подсчета частоты встречаемости чисел
    digit_counts = {}

    # Подсчитываем количество каждой цифры в строке
    for digit in s:
        if digit.isdigit():
            digit = int(digit)
            digit_counts[digit] = digit_counts.get(digit, 0) + 1

    # Сортируем словарь по убыванию частоты встречаемости и выбираем три самых часто встречаемых числа
    most_common_digits = sorted(digit_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    # Создаем словарь из трех самых часто встречаемых чисел
    result = {digit: count for digit, count in most_common_digits}

    # Выводим значения в порядке возрастания ключа
    for digit in sorted(result.keys()):
        print(f"{digit}: {result[digit]}")

    # Возвращаем словарь
    return result

# Пример использования функции
s = "33415588990327"
result = count_digits(s)
print("Словарь из трех самых часто встречаемых чисел:", result)