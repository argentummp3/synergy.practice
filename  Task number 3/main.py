"""  Кейс-задача № 3  """

def find_sum_between_min_max(arr):
    if len(arr) < 2:
        return 0  # Если меньше 2 элементов, между ними ничего нет

    # Находим индексы минимального и максимального элементов
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))

    # Определяем границы диапазона "между"
    start = min(min_idx, max_idx) + 1
    end = max(min_idx, max_idx)

    # Суммируем отрицательные элементы в диапазоне
    total = 0
    for i in range(start, end):
        if arr[i] < 0:
            total += arr[i]

    return total


# Основная программа
N = int(input("Введите размер массива N: "))
A = []

print("Введите элементы массива:")
for i in range(N):
    element = float(input(f"Элемент {i + 1}: "))
    A.append(element)

result = find_sum_between_min_max(A)

print(f"Сумма отрицательных элементов между минимальным и максимальным: {result}")