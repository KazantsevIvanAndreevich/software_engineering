def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count

# Функция для замены слова "ugly" на "beauty"
def replace_word(sentence):
    return sentence.replace("ugly", "beauty")

# Функция для проверки начала строки на "The" или "епd"
def starts_with(sentence):
    return sentence.startswith("The") or sentence.startswith("епd")

# Получение предложения от пользователя
sentence = input("Введите предложение на английском: ")

# Вывод длины предложения
print("Длина предложения:", len(sentence))

# Перевод предложения в нижний регистр
print("Предложение в нижнем регистре:", sentence.lower())

# Подсчет количества гласных
vowels_count = count_vowels(sentence)
print("Количество гласных в предложении:", vowels_count)

# Замена слов "ugly" на "beauty"
new_sentence = replace_word(sentence)
print("Предложение с замененными словами:", new_sentence)

# Проверка начала строки на "The" или "епd"
if starts_with(sentence):
    print("Предложение начинается с 'The' или 'епd'")
else:
    print("Предложение не начинается с 'The' или 'епd'")