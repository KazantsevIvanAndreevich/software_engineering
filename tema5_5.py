def create_sets(input_list):
    # Создаем словарь для хранения количества повторений каждого числа
    num_counts = {}
    for num in input_list:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    
    # Создаем множество для хранения уникальных значений и строк-повторений
    result_set = set()
    for num, count in num_counts.items():
        # Добавляем число в множество
        result_set.add(num)
        # Добавляем строки-повторения числа в множество
        for i in range(2, count + 1):
            result_set.add(str(num) * i)
    
    return result_set

# Тестовые множества
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

# Вывод результатов
print(create_sets(list_1))
print(create_sets(list_2))
print(create_sets(list_3))