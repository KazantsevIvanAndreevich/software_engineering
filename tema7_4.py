def censor_sentence(sentence, forbidden_words):
    words = sentence.split()  # Разбиваем предложение на слова
    censored_words = []  # Здесь будем хранить слова с заменой

    for word in words:
        # Проверяем, является ли слово запрещенным
        if word.lower() in forbidden_words:
            # Если да, заменяем его звездочками
            censored_words.append('*' * len(word))
        else:
            # Если нет, оставляем слово без изменений
            censored_words.append(word)

    # Собираем предложение из цензурированных слов
    censored_sentence = ' '.join(censored_words)
    return censored_sentence

# Запрещенные слова
forbidden_words = ['hello', 'email', 'python', 'the', 'exam', 'wor', 'is']

# Предложение для проверки
sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"

# Применяем цензуру к предложению
censored_result = censor_sentence(sentence, forbidden_words)
print("Результат:", censored_result)