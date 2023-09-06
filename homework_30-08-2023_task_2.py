'''
Задача № 2: Напишите функцию для транспонирования матрицы
'''

import numpy as np #### только для создания случайной матрицы для проверки функции транспонирования

def t_(matrix):
    # Подсчет числа строк и столбцов во входной матрице
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    # Создание новой матрицы для транспонирования
    transposed_matrix = []

    # Цикл по столбцам входной матрицы для перемещения из в строки новой матрицы
    for col in range(num_cols):
        transposed_row = []
        for row in range(num_rows):
            transposed_row.append(matrix[row][col])
        transposed_matrix.append(transposed_row)

    return transposed_matrix

### Создание случайной матрицы
num_rows = int(input("Введите желаемое количество строк: "))
num_columns = int(input("Введите желаемое количество столбцов: "))

random_matrix = np.random.randint(1, 10, size=(num_rows, num_columns))

print('\nИсходная матрица:\n')
print(random_matrix)

print('\nТранспонированная матрица:\n')
result_matrix = t_(random_matrix)
for row in result_matrix:
    print(row)
