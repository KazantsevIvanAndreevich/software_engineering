def add_two(number):
    try:
        result = 2 + int(number)
        print("Результат сложения: ", result)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

# Тесты с корректным вводом
print("Тесты с корректным вводом:")
add_two(5)
add_two(10)

# Тесты с некорректным вводом
print("\nТесты с некорректным вводом:")
add_two("abc")
add_two([1, 2, 3])