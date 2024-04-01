from tema4_5_triangle_area import calculate_triangle_area

def get_input():
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    return a, b, c

def main():
    a, b, c = get_input()
    area = calculate_triangle_area(a, b, c)
    print("Площадь треугольника:", area)

if __name__ == "__main__":
    main()