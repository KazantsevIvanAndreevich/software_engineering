text = input("Введите текст: ")
word = input("Введите слово для поиска: ")
count = text.lower().count(word.lower())
print(f"Слово '{word}' встречается в тексте {count} раз.")