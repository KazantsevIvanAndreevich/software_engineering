def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as file:
        for _ in range(n):
            file.write(str(a) + "\n")
            yield a
            a, b = b, a + b

# Генерация первых 200 чисел Фибоначчи с записью в файл
fibonacci_sequence = fib(200)

# Вывод чисел Фибоначчи от 200
for num in fibonacci_sequence:
    print(num)