import math

def calculate_z(x, y):
    z = math.cos(x) ** 2 + math.sin(y) ** 2
    return z

def sum_of_squares(N):
    total = sum(i ** 2 for i in range(1, N + 1))
    return total

def main():
    x = float(input("Введіть значення x (у радіанах): "))
    y = float(input("Введіть значення y (у радіанах): "))
    z = calculate_z(x, y)
    print(f"Результат обчислення z = (cos(x))^2 + (sin(y))^2: {z}")

    N = int(input("Введіть ціле число N: "))
    if N > 0:
        S = sum_of_squares(N)
        print(f"Сума квадратів чисел від 1 до {N}: {S}")
    else:
        print("Число N повинно бути додатнім!")

if __name__ == "__main__":
    main()
