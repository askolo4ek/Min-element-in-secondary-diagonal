import random

#Ввод данных с проверкой, что N>=3 и N - целочисленное
while True:
    try:
        N = int(input("Введите целое число N>=3: "))
    except ValueError:
        print("Ошибка! N меньше 3 или неправильный формат ввода!")
        continue

    if N >= 3:
        break
    else:
        print("Ошибка! N меньше 3 или неправильный формат ввода!")

#Создание двумерной матрицы N*N и заполнение рандомными числами
matrix = [random.randint(-100, 100) for _ in range(N*N)]
matrix = [matrix[i*N:i*N+N] for i in range(N)]

#Поиск минимума побочной диагонали в матрице
minimum = float('+inf')
for i in range(N):
    if matrix[i][N-i-1] < minimum:
        minimum = matrix[i][N-i-1]

print(minimum)

