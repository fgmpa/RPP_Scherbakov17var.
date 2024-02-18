import numpy as np


def inputelem():
    N = np.random.randint(2, 5) # вводим кол-во строк
    M = np.random.randint(2, 5) # вводим кол-во столбцов
    A = np.random.randint(10, size=(N,M)) # задаем матрицу размером NxM
    B = np.random.randint(10, size=(M)) # задаем строку длиной M
    print("Матрица A = : \n", A) # выводим исходную матрицу А
    print("Строка B = : ", B) # выводим сгенерированную строку В
    L = np.random.randint(2,5) # случайным образом выбираем номер строки
    print("Num stroki:", L) # выводим номер строки
    A = np.insert(A, [L-1], B, axis=0) #вставляем строку В под номером L-1, так как отсчет от нуля
    print("Новая матрица: ", A) #Выводим новую матрицу А
    np.savetxt('lab2.txt', A, fmt='%d') # сохраняем данные в файл


inputelem()