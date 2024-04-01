def find_unique_elements(lst):
    unique_elements = set(lst)  # Преобразуем список в множество для удаления дубликатов
    sorted_unique = sorted(unique_elements)  # Сортируем уникальные элементы
    return sorted_unique

# Тесты
tests = [
    ([3, 1, 2, 2, 4, 3], [1, 2, 3, 4]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([9, 8, 8, 7, 6, 6, 5, 5], [5, 6, 7, 8, 9])
]

for lst, expected_result in tests:
    result = find_unique_elements(lst)
    assert result == expected_result, f"Ожидаемый результат: {expected_result}, Полученный результат: {result}"
    print("Исходный список:", lst)
    print("Отсортированные уникальные элементы:", result)
    print()

print("Все тесты пройдены успешно!")