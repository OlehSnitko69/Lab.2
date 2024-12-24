import math
from myOwnModule import sum_of_squares

def calculate_z(x, y):
    z = math.cos(x)**2 + math.sin(y)**2
    return z

def main():
    try:
        x = float(input("Введіть значення x (у радіанах): "))
        y = float(input("Введіть значення y (у радіанах): "))
        z = calculate_z(x, y)
        print(f"Результат обчислення z = (cos(x))^2 + (sin(y))^2: {z}")
    except ValueError:
        print("Помилка! Введіть коректні числові значення.")

    try:
        N = int(input("Введіть ціле число N: "))
        S = sum_of_squares(N)
        print(f"Сума квадратів чисел від 1 до {N}: {S}")
    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
