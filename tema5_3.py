# Импортируем библиотеку math для вычисления квадратного корня
import math

# Три списка с длинами сторон треугольников
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

# Находим максимальный и минимальный элементы в каждом списке
max_one = max(one)
min_one = min(one)
max_two = max(two)
min_two = min(two)
max_three = max(three)
min_three = min(three)

# Функция для вычисления площади треугольника по формуле Герона
def area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Находим площадь треугольников с максимальными и минимальными сторонами
area_max = area(max(max_one, max_two, max_three), 
                min(max_one, max_two, max_three), 
                min(max_one, max_two, max_three))
area_min = area(max(min_one, min_two, min_three), 
                min(min_one, min_two, min_three), 
                min(min_one, min_two, min_three))

# Выводим результаты
print("Площадь треугольника с максимальными сторонами:", area_max)
print("Площадь треугольника с минимальными сторонами:", area_min)