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