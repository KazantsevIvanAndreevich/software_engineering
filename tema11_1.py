def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Генерация первых 200 чисел Фибоначчи
fibonacci_sequence = fib(200)

# Вывод чисел Фибоначчи от 200
for num in fibonacci_sequence:
    print(num)