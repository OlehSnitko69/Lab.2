def sum_of_squares(N):

    if N <= 0:
        raise ValueError("Число N повинно бути додатнім!")
    total = sum(i**2 for i in range(1, N + 1))
    return total
