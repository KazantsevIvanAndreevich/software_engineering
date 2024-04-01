def count_statistics(file_name):
    # Инициализация счетчиков
    letters_count = 0
    words_count = 0
    lines_count = 0

    # Открываем файл и читаем его построчно
    with open(file_name, 'r') as file:
        for line in file:
            # Обновляем счетчики для каждой строки
            letters_count += len([char for char in line if char.isalpha()])
            words_count += len(line.split())
            lines_count += 1

    # Выводим результаты
    print("Input file contains:")
    print(f"{letters_count} letters")
    print(f"{words_count} words")
    print(f"{lines_count} lines")

# Имя файла
file_name = "input.txt"

# Вызываем функцию для подсчета статистики
count_statistics(file_name)