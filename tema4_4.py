def average(*args):
    if len(args) == 0:
        return 0
    
    total = sum(args)
    return total / len(args)

if __name__ == "__main__":
    values = [int(x) for x in input("Введите числа через пробел: ").split()]
    result = average(*values)
    print("Среднее арифметическое:", result)