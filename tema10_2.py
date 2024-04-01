def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            if not data:
                raise Exception("файл пустой")
            else:
                print("Информация из файла:")
                print(data)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(e)

# Создание пустого файла
with open("empty_file.txt", "w") as file:
    pass

# Создание файла с информацией
with open("data_file.txt", "w") as file:
    file.write("Казанцев Иван Андреевич")

# Попытка чтения пустого файла
print("Попытка чтения пустого файла:")
read_file("empty_file.txt")

# Попытка чтения файла с информацией
print("\nПопытка чтения файла с информацией:")
read_file("data_file.txt")