num_subjects = int(input("Введите количество предметов: "))
total_score = 0
for i in range(num_subjects):
    score = float(input(f"Введите оценку за предмет {i + 1}: "))
    total_score += score
average_score = total_score / num_subjects
print(f"Средняя оценка за {num_subjects} предметов: {average_score}")