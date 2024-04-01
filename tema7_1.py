from collections import Counter
import re

def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text.lower())  # Извлекаем слова из текста и приводим их к нижнему регистру
            word_count = len(words)
            most_common_word = Counter(words).most_common(1)[0]  # Находим самое часто встречающееся слово
            return word_count, most_common_word
    except FileNotFoundError:
        return "Файл не найден"

# Пример использования
filename = r'D:\desktop\УрГЭУ\Контрольные\Программная инженерия\СР7\test7.txt'  # Укажите путь к вашему файлу
word_count, most_common_word = count_words(filename)
print(f"Количество слов в файле: {word_count}")
print(f"Самое часто встречающееся слово: '{most_common_word[0]}' (встречается {most_common_word[1]} раз)")