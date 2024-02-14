import random


def getget_numnumbers():
    num = int(input("Введите число 1 для ручной реализации, для стандартной реализации - 2: "))
    print(num)

    A = []

    if num == 1:
        maxmin_elems()
    else:
        result = remove_elements(A)
        print(result)  # [9, 4, 1, 0, 0]

    return A


def remove_elements(A):

    # Исходный список чисел
    A = get_numbers()

    # Найдем индексы минимального и максимального элементов в списке
    min_index = A.index(min(A))
    max_index = A.index(max(A))

    # Если минимальный элемент стоит после максимального, поменяем их местами
    if min_index > max_index:
        min_index, max_index = max_index, min_index

    # Удаляем элементы с четными индексами между минимальным и максимальным элементами
    del A[min_index+1:max_index:2]

    return A[::2]  # Возвращаем список с элементами на нечетных позициях (т.е. с удаленными четными)


def get_numbers():
    num = int(input("Введите число 1 для ручного ввода, для автоматической генерации - 2: "))
    print(num)

    A = []

    if num == 1:
        A = input().split()
        print("Массив A: ", A)
    else:
        N = int(input("Введите размер массива A: "))
        for i in range(N):
            A.append(random.randint(1, 9))
        print("Массив A: ", A)

    return A


def maxmin_elems():
    # Исходный список чисел
    A = get_numbers()

    # Инициализация переменной max_number and min_number
    max_number = A[0]
    min_number = A[0]
    index_min = 0
    index_max = 0

    # Цикл for для нахождения мин и макс элементов и их индексов
    for i, number in enumerate(A[1:], 1):
        if number > max_number:
            max_number = number
            index_max = i

        if number < min_number:
            min_number = number
            index_min = i
    # Если сначала в списке мин элемент, а потом макс, то нужно между ними удалить элементы с четным индексом

    index_start = 0
    index_end = 0

    if index_min > index_max:
        index_start = index_max
        index_end = index_min
    else:
        index_start = index_min
        index_end = index_max

    for i in range(index_end - 1, index_start, -1):
        if (i + 1) % 2 == 0:
            del A[i]
            i -= 1

    # Вывод максимального числа
    print("Максимальное число в списке:", max_number)
    # Вывод минимального числа
    print("Минимальное число в списке:", min_number)
    print('Итоговый   список: ', A)


getget_numnumbers()