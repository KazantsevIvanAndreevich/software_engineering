# Списки оценок
grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

# Удаляем все двойки из списка и заменяем тройки на четверки
grades1 = [grade for grade in grades1 if grade != 2]
grades1 = [4 if grade == 3 else grade for grade in grades1]

grades2 = [grade for grade in grades2 if grade != 2]
grades2 = [4 if grade == 3 else grade for grade in grades2]

grades3 = [grade for grade in grades3 if grade != 2]
grades3 = [4 if grade == 3 else grade for grade in grades3]

# Выводим обновленные списки оценок
print("Обновленный список оценок 1:", grades1)
print("Обновленный список оценок 2:", grades2)
print("Обновленный список оценок 3:", grades3)