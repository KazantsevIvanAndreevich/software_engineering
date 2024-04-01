import random

def roll_dice():
    roll = random.randint(1, 6)
    print(f"Бросок кубика: {roll}")

    if roll >= 5:
        print("Вы победили")
    elif roll >= 3:
        roll_dice()
    else:
        print("Вы проиграли")

if __name__ == "__main__":
    roll_dice()