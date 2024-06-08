# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Матрицы ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Перебор элементов матрицы  ===========================================================================================
# Перебор по строкам:
rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов

matrix = [
    [2, 3, 1, 0],
    [9, 4, 6, 8],
    [4, 7, 2, 7],
]

for r in range(rows):  # кол-во строк
    for c in range(cols):  # кол-во столбцов
        print(matrix[r][c], end=' ')
    print()

# 2 3 1 0
# 9 4 6 8
# 4 7 2 7


# Перебор по столбцам:
rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов

matrix = [
    [2, 3, 1, 0],
    [9, 4, 6, 8],
    [4, 7, 2, 7],
]

for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=' ')
    print()

# 2 9 4
# 3 4 7
# 1 6 2
# 0 8 7


# Метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста ===========================================
print('a'.ljust(3))
print('ab'.ljust(3))
print('abc'.ljust(3))

# a
# ab
# abc

print('a'.ljust(5, '*'))
print('ab'.ljust(5, '$'))
print('abc'.ljust(5, '#'))

# a****
# ab$$$
# abc##

# Пример:
rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов

matrix = [
    [277, -930, 11, 0],
    [9, 43, 6, 87],
    [4456, 8, 290, 7],
]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()

# 277   -930  11    0
# 9     43    6     87
# 4456  8     290   7


# Метод rjust()  выравнивает текст по ширине, добавляя пробелы в начало текста =========================================
print('a'.rjust(3))
print('ab'.rjust(3))
print('abc'.rjust(3))

#   a
#  ab
# abc

print('a'.rjust(5, '*'))
print('ab'.rjust(5, '$'))
print('abc'.rjust(5, '#'))

# ****a
# $$$ab
# ##abc


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Квадратные матрицы ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Матрица с одинаковым количеством строк и столбцов называется квадратной. У квадратной матрицы есть две диагонали:
# главная: проходит из верхнего левого в правый нижний угол матрицы.
# побочная: проходит из нижнего левого в правый верхний угол матрицы.

# Элементы с равными индексами row == c находятся на главной диагонали. Такие элементы обозначаются
# chessboard[row][row].
# Элементы с индексами row и c, связанными соотношением row + c + 1 = index_del (или c = index_del - row - 1), где
# index_del — размерность матрицы,
# находятся на побочной диагонали.


n = 8
matrix = [[0] * n for _ in range(n)]  # создаем квадратную матрицу размером 8×8

for i in range(n):  # заполняем главную диагональ единицами, а побочную двойками
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 2

for r in range(n):  # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()

# 1 0 0 0 0 0 0 2
# 0 1 0 0 0 0 2 0
# 0 0 1 0 0 2 0 0
# 0 0 0 1 2 0 0 0
# 0 0 0 2 1 0 0 0
# 0 0 2 0 0 1 0 0
# 0 2 0 0 0 0 1 0
# 2 0 0 0 0 0 0 1


n = 3
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for i in range(n):  # 0, 1, 2
    for j in range(n):  # 0, 1, 2
        print(a[n - i - 1][n - j - 1], end=' ')  # a[3 - 0 - 1][3 - 0 - 1] == 9, 8, 7
    print()


# 9 8 7
# 6 5 4
# 3 2 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 1:

# 4  # кол-во строки
# 2  # кол-во столбцов
# и
# швец
# и
# жнец
# и
# на
# дуде
# игрец

def matrix_constructor(n: int, m: int):
    matrix = [[input() for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()


if __name__ == '__main__':
    n, m = int(input()), int(input())
    matrix_constructor(n, m)


# и швец
# и жнец
# и на
# дуде игрец

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 2:

# 4  # кол-во строки
# 2  # кол-во столбцов
# и
# швец
# и
# жнец
# и
# на
# дуде
# игрец

def matrix_constructor(n: int, m: int):
    matrix = [[input() for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()

    print()

    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print()


if __name__ == '__main__':
    n, m = int(input()), int(input())
    matrix_constructor(n, m)


# и швец
# и жнец
# и на
# дуде игрец
#
# и и и дуде
# швец жнец на игрец

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 3:

# Найти сумму элементов главной диагонали квадратной матрицы:
# Ввод кол-ва строк и столбцов.
# Ввод матрицы.

# Пример:
# 3 - кол-во строк и столбцов
# 1 2 3 - ввод 1 строки матрицы
# 4 5 6 - ввод 2 строки матрицы
# 7 8 9 - ввод 3 строки матрицы

# Вывод: 15

def matrix_constructor(n: int):
    result = 0
    matrix = [input().split() for _ in range(n)]

    for i in range(n):
        result += int(matrix[i][i])

    return result


if __name__ == '__main__':
    n = int(input())
    obj_matrix_constructor = matrix_constructor(n)
    print(obj_matrix_constructor)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 4:


def above_average(number_rows_col: int):
    matrix = [list(map(int, input().split())) for _ in range(number_rows_col)]
    num_num = 0

    for row in matrix:
        for column in row:
            if column > sum(row) / number_rows_col:
                num_num += 1

        print(num_num)
        num_num = 0


if __name__ == '__main__':
    number_rows_col = int(input())
    above_average(number_rows_col)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 5:

# Найти максимальное число по нижней диагонали:

def maximum_in_area(number_rows_col: int):
    matrix = [list(map(int, input().split())) for _ in range(number_rows_col)]

    n = 0
    len_matrix = len(matrix)
    res_num = matrix[0][0]

    for row in matrix:
        n += 1
        if n > len_matrix:
            break
        for col in row[:n]:
            if col > res_num:
                res_num = col

    return res_num


if __name__ == '__main__':
    number_rows_col = int(input())
    print(maximum_in_area(number_rows_col))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 6:

# Найти максимальное число по диагоналям с левой и правой стороной:


def maximum_in_area_2(number_rows_col: int):
    matrix = [list(map(int, input().split())) for _ in range(number_rows_col)]
    res_num = matrix[0][0]
    n = len(matrix) / 2
    f = 0

    if number_rows_col % 2 != 0:
        n += 1
    if number_rows_col <= 2:
        for i in matrix:
            for j in i:
                if j > res_num:
                    res_num = j
        return res_num
    else:
        ind = 0
        ind_2 = -1

        for row in matrix:
            f += 1
            if f > n:
                ind -= 1
                ind_2 += 1
            else:
                ind += 1
                ind_2 -= 1

            if ind == 0:
                break
            for col in row[0:ind]:
                if col > res_num:
                    res_num = col
            for col2 in row[-1:ind_2: -1]:
                if col2 > res_num:
                    res_num = col2

    return res_num


if __name__ == '__main__':
    number_rows_col = int(input())
    print(maximum_in_area_2(number_rows_col))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 7:

def quarter_amounts(num_rows_col: int) -> str:
    matrix = [
        [1, 4, 3, 4, 7],
        [5, 6, 7, 8, 4],
        [3, 8, 5, 6, 1],
        [1, 2, 9, 4, 8],
        [5, 6, 1, 5, 8],
    ]
    up = 0
    right = 0
    down = 0
    left = 0

    for i in range(num_rows_col):
        for j in range(num_rows_col):
            if i < j and i < (num_rows_col - 1 - j):
                up += matrix[i][j]
            elif j > i > (num_rows_col - 1 - j):
                right += matrix[i][j]
            elif i > j and i > (num_rows_col - 1 - j):
                down += matrix[i][j]
            elif j < i < (num_rows_col - 1 - j):
                left += matrix[i][j]

    return (f"Верхняя четверть: {up}\n"
            f"Правая четверть: {right}\n"
            f"Нижняя четверть: {down}\n"
            f"Левая четверть: {left}")


if __name__ == '__main__':
    num_rows_col = 5
    print(quarter_amounts(num_rows_col))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 7:
# Найти номер строки и столбца максимального числа:

def maximum_in_table(n: int, m: int) -> (int, int):
    matrix = [list(map(int, input().split())) for _ in range(n)]
    req_row = 0
    req_col = 0
    maxx_num = matrix[0][0]

    for index_row, num_row in enumerate(matrix):
        for index_col, num_col in enumerate(num_row):
            if num_col > maxx_num:
                maxx_num = num_col
                req_row = index_row
                req_col = index_col

    print(req_row, req_col)


if __name__ == '__main__':
    n, m = int(input()), int(input())
    obj_maximum_in_table = maximum_in_table(n, m)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 8:
# Обмен столбцов местами:

def exchange_columns(row: int, col: int) -> (int, int):
    matrix = [list(map(int, input().split())) for _ in range(row)]
    num_col_for_exc = [list(map(int, input().split())) for i in range(1)]
    i = num_col_for_exc[0][0]
    j = num_col_for_exc[0][1]

    for x in matrix:
        x[i], x[j] = x[j], x[i]
        for y in x:
            print(y, end=' ')
        print()


if __name__ == '__main__':
    n, m = int(input()), int(input())
    obj_exchange_columns = exchange_columns(n, m)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 9:
# Ход коня на шахматной доске:

user_move = input()

chessboard = [j + str(i) for i in range(8, 0, -1) for j in "abcdefgh"]
index_move = chessboard.index(user_move)
ind_row = index_move // 8
ind_col = index_move % 8

matrix_2 = [["." for _ in range(8)] for _ in range(8)]
matrix_2[ind_row][ind_col] = "N"

if ind_row - 2 >= 0 and ind_col - 1 >= 0:
    matrix_2[ind_row - 2][ind_col - 1] = "*"
if ind_row - 2 >= 0 and ind_col + 1 <= 7:
    matrix_2[ind_row - 2][ind_col + 1] = "*"
if ind_row + 2 <= 7 and ind_col - 1 >= 0:
    matrix_2[ind_row + 2][ind_col - 1] = "*"
if ind_row + 2 <= 7 and ind_col + 1 <= 7:
    matrix_2[ind_row + 2][ind_col + 1] = "*"

if ind_row - 1 >= 0 and ind_col - 2 >= 0:
    matrix_2[ind_row - 1][ind_col - 2] = "*"
if ind_row - 1 >= 0 and ind_col + 2 <= 7:
    matrix_2[ind_row - 1][ind_col + 2] = "*"
if ind_row + 1 <= 7 and ind_col - 2 >= 0:
    matrix_2[ind_row + 1][ind_col - 2] = "*"
if ind_row + 1 <= 7 and ind_col + 2 <= 7:
    matrix_2[ind_row + 1][ind_col + 2] = "*"

for i in matrix_2:
    for j in i:
        print(j, end=" ")
    print()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 10:
# Проверить, чтобы сумма каждой строки, столбца, диагонали квадратной матрицы была равна:

def magic_square(size: int) -> str:
    matrix_square = [list(map(int, input().split())) for _ in range(size)]
    matrix_square_in_line = []

    for row in matrix_square:
        for col in row:
            matrix_square_in_line.append(col)

    control_sum = sum(matrix_square_in_line) / size
    # ------------------------
    if 0 in matrix_square_in_line or len(set(matrix_square_in_line)) != size ** 2:
        return "NO"
    else:
        for row in matrix_square:
            if sum(row) != control_sum:
                return "NO"
    # ------------------------
    index = 0
    index_2 = -1
    sum_diagonal = 0
    sum_diagonal_2 = 0

    while index < size:
        sum_diagonal += matrix_square[index][index]
        sum_diagonal_2 += matrix_square[index][index_2]

        index += 1
        index_2 -= 1

    if sum_diagonal != control_sum or sum_diagonal_2 != control_sum:
        return "NO"
    # ------------------------
    index_3 = 0
    sum_col = 0
    for _ in range(size):
        for _ in range(size):
            sum_col += matrix_square_in_line[index_3]
            index_3 += size
        if sum_col != control_sum:
            return "NO"
        else:
            index_3 = 1
            sum_col = 0
    # ------------------------
    return "YES"


if __name__ == '__main__':
    size_square = int(input())
    obj_magic_square = magic_square(size_square)
    print(obj_magic_square)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задача 11:
# Шахматное поле из * и .:


def chessboard(size_r: int, size_c: int) -> None:
    dot = "."
    star = "*"

    while size_r > 0:
        for i in range(size_c):
            print(dot, end=" ")
            if size_c == 1:
                continue
            else:
                dot, star = star, dot

        print()
        dot, star = star, dot
        size_r -= 1


if __name__ == '__main__':
    size_row, size_col = map(int, input().split(" "))
    chessboard(size_row, size_col)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Операции над матрицами ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Сложение матриц ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

matrixA = [[2, -3, 1], [5, 4, -2]]  # матрица 1
matrixB = [[4, 2, -5], [-4, 1, 3]]  # матрица 2

matrixC = []  # матрица 3, для суммы 2-х матриц

for i in range(len(matrixA)):  # берем индекс для списка внутри матрицы
    matrixC.append([])  # добавление нового пустого списка в матрицу
    for j in range(len(matrixA[0])):  # берем индекс для элемента внутри списка матрицы
        matrixC[i].append(matrixA[i][j] + matrixB[i][j])
        # добавляем в список матрицы с индексом [0] суммы матриц значений с индексами [0], [0] первых 2-х матриц.

print(matrixC)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def matrix_addition(mtrx1: list[list], mtrx: list[list]):
    res_matrix = []

    for row in range(len(mtrx1)):
        res_matrix.append([])
        for col in range(len(mtrx1[0])):
            res_matrix[row].append(mtrx1[row][col] + mtrx[row][col])

    for row in res_matrix:
        for col in row:
            print(str(col).ljust(2), end="")
        print()


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    input()
    matrix2 = [list(map(int, input().split())) for _ in range(n)]
    matrix_addition(matrix, matrix2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Свойства сложения матриц:

# Коммутативность – результат сложения матриц не зависит от их перестановки:
# A+B=B+A;

# Ассоциативность – результат сложения матриц не зависит от расстановки скобок:
# A+(B+C)=(A+B)+C;

# Сложение с нулевой матрицей – для любой матрицы существует нейтральный элемент, которым является нулевая матрица,
# сложение с которым не изменяет исходную матрицу. Нулевая матрица – матрица, все элементы которой имеют
# нулевое значение:
# A+0=0+A=A;

# Существование противоположной матрицы – для ненулевой матрицы A всегда есть матрица −A, сложение с которой даст
# в результате нулевую матрицу:
# A+(−A)=0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Умножение матрицы на число ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

matrixA = [[5, -2, 4], [3, 1, -3]]
k = 7

for i in range(len(matrixA)):
    for j in range(len(matrixA)):
        matrixA[i][j] = matrixA[i][j] * k
        # переназначаем значения матрицы на умноженное на 7

print(matrixA)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Свойства умножения матрицы на число:

# Единица – нейтральное число умножения любой матрицы, результат умножения на нейтральное число – исходная матрица:
# 1×A=A;

# Результат умножения любой матрицы на ноль – нулевая матрица, все элементы которой равны нулю:
# 0×A=0;

# Для матриц одного размера и действительного числа выполняется свойство дистрибутивности умножения относительно
# сложения:
# k×(A+B)=k×A+k×B;

# Для любой матрицы и суммы действительных чисел выполняется свойство дистрибутивности:
# (k+n)×A=k×A+n×A;

# Для любой матрицы и произведения любых действительных чисел выполняется свойство ассоциативности умножения:
# (k×n)×A=k×(n×A).


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Умножение матрицы на матрицу ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Умножение двух матриц A и B – вычисление результирующей матрицы C, каждый элемент c[i][j] которой равен сумме
# произведений элементов соответствующих строки первой матрицы a[i][r] и столбца второй матрицы b[r][j]

# То есть матрицы должны быть согласованы по размерности. Результат
# умножения матрицы размера n×m на матрицу размером m×k – матрица размером n×k.

# !!! Одну матрицу можно умножать на другую только тогда, когда количество столбцов в первой матрице совпадает с
# количеством строк во второй матрице. !!!

matrixA = [[2, -3, 1], [5, 4, -2]]
matrixB = [[-7, 5], [2, -1], [4, 3]]

matrixC = []

res = []
n = 0
while len(matrixC) < len(matrixA):
    matrixC.append([])

    for i in range(len(matrixA)):
        for j in range(len(matrixB)):
            res.append(matrixA[n][j] * matrixB[j][i])

        matrixC[n].append(sum(res))
        res = []

    n += 1

print(matrixC)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def matrix_multiplication(mtrx1: list[list], mtrx2: list[list]):
    mult_matrix = []  # Итоговая матрица;
    temp = []  # Промежуточный список, для суммы перемноженных значений;
    counter_index = 0  # Счетчик - индекс для первой матрицы и итоговой матрицы;

    # ----------------------------

    while len(mult_matrix) < len(mtrx1):  # цикл, пока длина итоговой матрицы меньше длины первой матрицы;
        mult_matrix.append([])  # добавление пустого списка в итоговую матрицу;

        for row in range(len(mtrx1)):
            for col in range(len(mtrx2)):
                temp.append(mtrx1[counter_index][col] * mtrx2[col][row])
                # добавление в промежуточный список перемноженных значений;

            mult_matrix[counter_index].append(sum(temp))
            # добавление в итоговый список с индексом counter_index, суммы значений из промежуточного списка;
            temp.clear()  # очищение промежуточного списка;

        counter_index += 1  # увеличение счетчика на 1;

    # ----------------------------

    for row in mult_matrix:  # разворачивание итоговой матрицы;
        for col in row:
            print(col, end=" ")
        print()

    # ----------------------------


if __name__ == '__main__':  # вводные значения;
    n, m = map(int, input().split())  # переменная m не нужна в коде, но для условия задачи ввёл!!!;
    matrix1 = [list(map(int, input().split())) for _ in range(n)]
    input()
    n2, m2 = map(int, input().split())  # переменная m2 не нужна здесь тоже!!!;
    matrix2 = [list(map(int, input().split())) for _ in range(n2)]
    matrix_multiplication(matrix1, matrix2)  # вызов функции.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(m)]
matrixC = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for q in range(m):
            matrixC[i][j] += matrixA[i][q] * matrixB[q][j]

for row in matrixC:
    print(*row)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Возведение в степень матрицы:

def matrix_exponentiation(mtrx: list[list], mtrx2: list[list]) -> list[list]:
    mult_matrix = []
    temp = []
    counter_index = 0

    while len(mult_matrix) < len(mtrx):
        mult_matrix.append([])

        for row in range(len(mtrx)):
            for col in range(len(mtrx2)):
                temp.append(mtrx[counter_index][col] * mtrx2[col][row])

            mult_matrix[counter_index].append(sum(temp))
            temp.clear()

        counter_index += 1

    return mult_matrix


if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    matrix2 = matrix
    m = int(input())

    while m > 1:
        matrix = matrix_exponentiation(matrix, matrix2)
        m -= 1

    for i in matrix:
        print(*i, end="\n")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def every_element(symbols: str, quantity_array: int) -> list[list]:
    """Задание: На вход программе подается строка текста, содержащая символы и число n.
    Из данной строки формируется список. Напишите программу, которая разделяет
    список на вложенные подсписки так, что n последовательных элементов принадлежат
    разным подспискам."""

    result_array = []
    count = 0

    while count < quantity_array:
        result_array.append([])
        for i in symbols[count::quantity_array]:
            result_array[count].append(i)

        count += 1

    return result_array


if __name__ == '__main__':
    text, num = [input().split() for i in range(2)]
    func_every_element = every_element(text, int(*num))
    print(func_every_element)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def maximum_in_area(quantity: int) -> int:
    """Напишите программу, которая выводит максимальный элемент в нижней части побочной диагонали (включительно)
    области квадратной матрицы."""

    matrix = [list(map(int, input().split())) for _ in range(quantity)]

    result_array = []

    for index, element in enumerate(matrix):
        for element_2 in element[-(index + 1)::]:
            result_array.append(element_2)

    return max(result_array)


if __name__ == '__main__':
    quantity_row_col = int(input())
    func_maximum_in_area = maximum_in_area(quantity_row_col)
    print(func_maximum_in_area)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def matrix_transposition(quantity: int) -> None:
    """Напишите программу, которая транспонирует квадратную матрицу."""

    matrix = [list(map(int, input().split())) for _ in range(quantity)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[j][i], end=" ")
        print()


if __name__ == '__main__':
    quantity_row_col = int(input())
    matrix_transposition(quantity_row_col)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def snowflake(quantity: int) -> None:
    """На вход программе подается нечетное натуральное число n. Напишите программу,
    которая создает матрицу размером n×n заполнив её символами '.', затем заполните
    символами '*' среднюю строку и столбец матрицы, главную и побочную диагональ матрицы.
    Выведите полученную матрицу на экран, разделяя элементы пробелами."""

    matrix = [["."] * quantity for _ in range(quantity)]

    for index in range(quantity):
        matrix[index][index] = "*"
        matrix[index][quantity - index - 1] = "*"
        matrix[quantity // 2][index] = "*"
        matrix[index][quantity // 2] = "*"

    for row in range(quantity):
        for col in range(quantity):
            print(matrix[row][col], end=' ')

        print()


if __name__ == '__main__':
    quantity_row_col = int(input())
    snowflake(quantity_row_col)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def symmetric_matrix(mtrx: list[list]) -> str:
    """Напишите программу проверки симметричности квадратной матрицы
    относительно побочной диагонали."""

    symm_mtrx = []
    length_mtrx = len(mtrx)

    for row in range(length_mtrx):
        symm_mtrx.append([])
        for col in range(length_mtrx):
            symm_mtrx[row].append(mtrx[col][row])

    for row in range(length_mtrx):
        symm_mtrx[row] = symm_mtrx[row][::-1]

    if mtrx == symm_mtrx[::-1]:
        return "YES"

    return "NO"


if __name__ == '__main__':
    quantity_row_col = int(input())
    matrix = [list(map(int, input().split())) for _ in range(quantity_row_col)]
    func_symmetric_matrix = symmetric_matrix(matrix)
    print(func_symmetric_matrix)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def latin_square(mtrx: list[list], quantity: int) -> str:
    """Латинским квадратом порядка n называется квадратная матрица
    размером n×n, каждая строка и каждый столбец которой содержат
    все числа от 1 до n. Напишите программу, которая проверяет,
    является ли заданная квадратная матрица латинским квадратом."""

    flag = "YES"

    control_array = []
    for num in range(1, quantity + 1):
        control_array.append(num)

    for row in mtrx:
        for num in control_array:
            if row.count(num) == 1:
                pass
            else:
                flag = "NO"
                break
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    array_col = []
    for index_row in range(quantity):
        for index_col in range(quantity):
            array_col.append(mtrx[index_col][index_row])

        for num in control_array:
            if array_col.count(num) == 1:
                pass
            else:
                flag = "NO"
                break

        array_col = []

    return flag


if __name__ == '__main__':
    quantity_row_col = int(input())
    matrix = [list(map(int, input().split())) for _ in range(quantity_row_col)]
    func_latin_square = latin_square(matrix, quantity_row_col)
    print(func_latin_square)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def queen_moves(queen_pos: str) -> None:
    """На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на
    доске и все клетки, которые бьет ферзь. Клетку, где стоит ферзь,
    отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *,
    остальные клетки заполните точками."""

    chessboard = [["."] * 8 for _ in range(8)]

    col = ord(queen_pos[0]) - ord('a')
    row = 8 - int(queen_pos[1])

    for i in range(len(chessboard)):
        for j in range(len(chessboard)):
            if i == row or j == col or abs(i - row) == abs(j - col):
                chessboard[i][j] = '*'

    chessboard[row][col] = 'Q'

    for i in chessboard:
        print(*i)


if __name__ == '__main__':
    queen_position = input().strip()
    queen_moves(queen_position)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def diagonals_parallel_to_the_main_one(*args) -> None:
    """На вход программе подается натуральное число n.
    Напишите программу, которая создает матрицу размером
    n×n и заполняет её по следующему правилу:
    на главной диагонали на месте каждого элемента должно стоять
    число 0; на двух диагоналях, прилегающих к главной, – число 1;
    на следующих двух диагоналях – число 2, и т.д."""

    quantity_row_col = int(input())
    matrix = [[0] * quantity_row_col for _ in range(quantity_row_col)]

    for row in range(quantity_row_col):
        for col in range(quantity_row_col):
            matrix[row][col] = abs(row - col)

    for row in matrix:
        print(*row)


if __name__ == '__main__':
    diagonals_parallel_to_the_main_one()
