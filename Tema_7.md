## Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Казанцев Иван Андреевич
- ИНО ЗБ ПОАС 22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
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
```
### Результат.
![Меню](https://github.com/KazantsevIvanAndreevich/software_engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/pic/tema2_1.png)

## Выводы
После выполнения программы в консоли будет выведена информация о количестве слов в файле и самом часто встречающемся слове.
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def load_expenses(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            expenses = {}
            for line in lines:
                category, amount = line.strip().split(':')
                if category not in expenses:
                    expenses[category] = []
                expenses[category].append(float(amount))
    except FileNotFoundError:
        expenses = {}
    return expenses

def save_expenses(file_name, expenses):
    with open(file_name, 'w') as file:
        for category, amounts in expenses.items():
            for amount in amounts:
                file.write(f"{category}:{amount}\n")

def add_expense(expenses, category, amount):
    if category not in expenses:
        expenses[category] = []
    expenses[category].append(amount)

def display_expenses(expenses):
    for category, amounts in expenses.items():
        total = sum(amounts)
        print(f"{category}: {total}")

def main():
    file_name = "expenses.txt"
    expenses = load_expenses(file_name)

    while True:
        print("\n1. Ввести новый расход")
        print("2. Показать текущие расходы")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            category = input("Введите категорию расхода: ")
            amount = float(input("Введите сумму расхода: "))
            add_expense(expenses, category, amount)
            save_expenses(file_name, expenses)
            print("Расход успешно добавлен!")
        elif choice == '2':
            print("\nТекущие расходы:")
            display_expenses(expenses)
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/KazantsevIvanAndreevich/software_engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/pic/tema2_2.png)

## Выводы
Данные о расходах сохраняются в текстовом файле expenses.txt. Каждая строка в файле представляет собой пару "категория:сумма". При запуске программы данные загружаются из этого файла, и пользователь может добавлять новые расходы или просматривать текущие. После каждого изменения данные сохраняются в файл.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 
• Текст в файле: 
Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex. 
Complex is better than complicated. 
• Ожидаемый результат: 
Input file contains: 
108 letters 
20 words 
4 lines

```python
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
```
### Результат.
![Меню](https://github.com/KazantsevIvanAndreevich/software_engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/pic/tema2_3.png)

## Выводы
ЭЭтот код открывает файл input.txt, читает его построчно и подсчитывает количество букв, слов и строк в тексте. Результаты выводятся в консоль.
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. 
• Запрещенные слова: hello email python the exam wor is 
• Предложение для проверки: Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!! 
• Ожидаемый результат: *****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
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
```
### Результат.
![Меню](https://github.com/KazantsevIvanAndreevich/software_engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/pic/tema2_4.png)

## Выводы
Этот код выполняет цензурирование предложения, заменяя запрещенные слова на звездочки. Вот пошаговое объяснение:

Функция censor_sentence(sentence, forbidden_words) принимает два аргумента: предложение (sentence) и список запрещенных слов (forbidden_words).
Предложение разбивается на отдельные слова с помощью метода split().
Затем происходит итерация по каждому слову из предложения.
  
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
Задача:
Напишите программу, которая будет анализировать текстовый файл с новостной статьей и выводить следующую статистику:
Количество слов в статье.
Количество предложений в статье.
Среднюю длину слова в статье.

```python
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
```
### Результат.
![Меню](https://github.com/KazantsevIvanAndreevich/software_engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/pic/tema2_5.png)

## Выводы
риведенный код выполняет следующие действия:

Определяется функция analyze_news_article, которая принимает путь к текстовому файлу в качестве аргумента.
Внутри функции файл открывается для чтения с помощью оператора with open(file_path, 'r', encoding='utf-8') as file:. Текст из файла считывается и сохраняется в переменную text.
Далее функция анализирует текст статьи:
Подсчитывает количество слов в статье, используя метод split() для разделения текста на слова по пробелам.
Определяет количество предложений в статье, используя методы count() для подсчета знаков препинания, таких как ".", "!" и "?".
Вычисляет среднюю длину слова в статье, делением общей длины всех слов на количество слов.
Функция возвращает количество слов, количество предложений и среднюю длину слова.
Затем указывается путь к текстовому файлу, который нужно проанализировать.
Функция analyze_news_article вызывается с этим путем, и результаты анализа выводятся в консоль.

## Общие выводы по теме

В ходе работы с файлами (вводом и выводом) мы узнали следующее:

Открытие файлов: Мы использовали функцию open() для открытия файлов. При этом указывали путь к файлу, режим открытия (чтение, запись, добавление и т. д.) и опционально указывали кодировку.

Чтение из файла: Для чтения текста из файла мы использовали метод read(), который считывает весь файл целиком, или метод readline(), который считывает одну строку из файла.

Запись в файл: Для записи текста в файл мы использовали метод write(), который записывает строку в файл.

Закрытие файла: После завершения работы с файлом важно закрыть его с помощью метода close(), чтобы освободить ресурсы операционной системы.

Работа с контекстным менеджером: Мы использовали конструкцию with open(...) as file, которая автоматически закрывает файл после завершения работы с ним.

Работа с содержимым файла: Мы читали содержимое файла, анализировали его, вносили изменения и записывали обратно в файл.
Работа с файлами является важной частью программирования, поскольку позволяет программам взаимодействовать с внешним хранилищем данных, что часто необходимо в реальных приложениях.

В целом, работа с числовыми и строковыми значениями является фундаментальной частью программирования, которая охватывает широкий спектр задач и является неотъемлемой частью создания практически любого программного решения.
