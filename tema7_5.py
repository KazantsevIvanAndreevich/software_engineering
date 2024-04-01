def analyze_news_article(file_path):
    # Открываем файл на чтение
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Получаем количество слов в статье
    word_count = len(text.split())

    # Получаем количество предложений в статье
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    # Получаем среднюю длину слова в статье
    words = text.split()
    average_word_length = sum(len(word) for word in words) / len(words)

    return word_count, sentence_count, average_word_length


# Путь к текстовому файлу
file_path = "Test7.txt"

# Анализируем новостную статью
word_count, sentence_count, average_word_length = analyze_news_article(file_path)

# Выводим статистику
print("Количество слов в статье:", word_count)
print("Количество предложений в статье:", sentence_count)
print("Средняя длина слова в статье:", round(average_word_length, 2))