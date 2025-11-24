""" Кейс-задача № 4 """

def max_dragon_power(N):
    if N <= 7:
        return N

    # Считаем количество троек
    num_threes = N // 3
    remainder = N % 3

    if remainder == 0:
        # Все тройки
        return 3 ** num_threes
    elif remainder == 1:
        # Заменяем одну тройку на две двойки (3*1 -> 2*2)
        return (3 ** (num_threes - 1)) * 4
    else:  # remainder == 2
        # Добавляем одну двойку
        return (3 ** num_threes) * 2


# Чтение входных данных
N = int(input())

# Вывод результата
print(max_dragon_power(N))