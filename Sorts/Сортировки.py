# Алгоритмы сортировки по сравнению:

# 1. Медленные:
# Пузырьковая сортировка (Bubble sort)
# Сортировка выбором (Selection sort)
# Сортировка простыми вставками (Insertion sort)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2. Быстрые:
# Сортировка Шелла (Shell sort)
# Быстрая сортировка (Quick sort)
# Сортировка слиянием (Merge sort)
# Пирамидальная сортировка (Heap sort)
# Сортировка TimSort (используется в Java и Python)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Алгоритмы сортировки НЕ по сравнению:

# Сортировка подсчетом (Counting sort)
# Блочная сортировка (Bucket sort)
# Поразрядная сортировка (Radix sort)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Квадратичная сложность (Квадратичная O(index_del^2)) - это форма описания временной сложности алгоритма, которая
# означает, что время выполнения алгоритма увеличивается пропорционально квадрату размера входных данных.

# Если алгоритм имеет квадратичную сложность, то при увеличении размера входных данных в 'number_pairs' раз, время
# выполнения алгоритма будет увеличиваться примерно в 'number_pairs^2' раз.

# Например, если у вас есть алгоритм с квадратичной сложностью и у вас увеличивается количество элементов для
# сортировки вдвое, то время, необходимое для выполнения этого алгоритма, увеличится приблизительно в четыре раза.
# Если количество элементов увеличится в три раза, время выполнения увеличится примерно в девять раз.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Сортировка пузырьком: Квадратичная O(index_del^2) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Алгоритм сортировки пузырьком состоит из повторяющихся проходов по сортируемому списку. За каждый проход элементы
# последовательно сравниваются попарно и, если порядок в паре неверный, выполняется обмен элементов. Проходы по списку
# повторяются number_pairs−1 раз, где number_pairs – длина списка.
# При каждом проходе алгоритма по внутреннему циклу, очередной наибольший элемент списка ставится на свое место в
# конце списка рядом с предыдущим «наибольшим элементом».

# Вкратце:
# При проходе первого list[number_pairs] элемента сравнивается каждый встречающий list[number_pairs+1] элемент и
# выполняется обмен элементов если порядок пар неверный, иначе если порядок пары встретился верный, то элемент
# остаётся на текущем месте и берется встретившийся элемент и продолжается прохождение до конца списка и далее, пока
# сортировка не завершится.

# 1 пример:
a = [5, 1, 4, 2, 8]
n = len(a)

for i in range(n - 1):
    finish = None
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            finish = True  # если во всех итерациях этого цикла не произошло изменений, то finish == None
            a[j], a[j + 1] = a[j + 1], a[j]

    if finish is None:
        break

print(a)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2 пример:
a2 = [
    17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17,
    36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20,
    -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56,
    -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21,
    -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84,
]

len_list = len(a2)

for i in range(len_list - 1):
    flag = None
    for j in range(len_list - i - 1):
        if a2[j] > a2[j + 1]:
            flag = True
            a2[j], a2[j + 1] = a2[j + 1], a2[j]

    if flag is None:
        break

print(a2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Сортировка выбором: Квадратичная O(index_del^2) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Сортировка выбором улучшает пузырьковую сортировку, совершая всего один обмен за каждый проход по списку.
# Для этого алгоритм ищет максимальный элемент и помещает его на соответствующую позицию. Как и для пузырьковой
# сортировки, после первого прохода самый большой элемент находится на правильном месте. После второго прохода на
# своё место становится следующий максимальный элемент. Проходы по списку повторяются number_pairs−1 раз, где
# number_pairs – длина списка, поскольку последний из них автоматически оказывается на своем месте.

# Вкратце:
# При проходе изначального list[number_pairs] элемента по списку, находится максимальный list(max[number_pairs])
# элемент и далее после прохода полностью list(max[number_pairs]) ставится на свое место (в начало или конец списка),
# а вместо list(max[number_pairs]) встает сравниваемый list[number_pairs], далее list[number_pairs+1] повторяет проход
# по списку, пока сортировка не завершится.

# 1 пример:
a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
     -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
     -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
     -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)

for i in range(n):
    index_min_number = 0
    min_prev_number = a[i]

    for j in range(i, n - 1):
        if a[j + 1] < a[i] and a[j + 1] < min_prev_number:
            index_min_number = j + 1
            min_prev_number = a[j + 1]

    if index_min_number:
        a[index_min_number], a[i] = a[i], a[index_min_number]

print(a)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Сортировка простыми вставками: Квадратичная O(index_del^2) ~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Алгоритм сортировки простыми вставками делит список на 2 части — отсортированную и неотсортированную.
# Из неотсортированной части извлекается очередной элемент и вставляется на нужную позицию в отсортированной части,
# в результате чего отсортированная часть списка увеличивается, а неотсортированная уменьшается. Так происходит,
# пока не исчерпан набор входных данных  и не отсортированы все элементы.

# Сортировка простыми вставками наиболее эффективна, когда список уже частично отсортирован и элементов
# массива немного. Если элементов в списке меньше 10, то этот алгоритм — один из самых быстрых.

# 1 пример:
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
n = len(a)

for i in range(1, n):
    elem = a[i]  # берем первый элемент из неотсортированной части списка

    # пока элемент слева существует и больше нашего текущего элемента
    while i >= 1 and a[i - 1] > elem:
        # смещаем c-й элемент отсортированной части вправо
        a[i] = a[i - 1]
        # сами идём влево, дальше ищем место для нашего текущего элемента
        i -= 1

    # нашли место для нашего текущего элемента из неотсортированной части
    # и вставляем его на индекс c в отсортированной части
    a[i] = elem

print('Отсортированный список:', a)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Болотная сортировка ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random
import time


def is_sort(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def bogosort(nums):
    while not is_sort(nums):
        random.shuffle(nums)
    return nums


numbers = list(range(10))
random.shuffle(numbers)
print(numbers)

start = time.time()

sorted_numbers = bogosort(numbers)
print(sorted_numbers)

end = time.time()

print(f"Секунд прошло: {(end - start).__round__(2)}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Разное ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from random import randint as r

array = [r(1, 20) for i in range(20)]  # Массив со случайными значениями в диапазоне.
print(array)


def sort_number(value):
    length_old_array = len(value) - 1
    iter_sort = True

    while iter_sort:
        iter_sort = False

        for index in range(length_old_array):
            if value[index] > value[index + 1]:
                t = value.pop(index)
                value.append(t)
                iter_sort = True

    return value


if __name__ == '__main__':
    print(sort_number(array))

# ---------------------
# Вставка в отсортированный массив:

sorted_old_array = [3, 4, 5, 6, 7, 8, 9, 11, 11, 12, 12, 13, 13, 17, 18, 19, 20, 21, 22, 23]
new_number = 14


def insert_in_array(s_array: list, n_num: int) -> str:
    for i in range(len(s_array)):
        if s_array[-1] <= n_num:  # Если последний элемент массива меньше, чем добавляемое число, то сразу в конец
            # массива добавляем и возврат.
            s_array.append(n_num)

            return f"Новый массив: {s_array}\nДлина нового массива: {len(s_array)}"

        if n_num > s_array[i]:
            pass
        else:
            s_array.insert(i, n_num)  # Иначе, перебираем массив, пока новое число меньше элемента, и вставляем его по
            # индексу предыдущего элемента массива.

            return f"Новый массив: {s_array}\nДлина нового массива: {len(s_array)}"


if __name__ == '__main__':
    print(f"Старый массив: {sorted_old_array}")
    print(f"Длина старого массива: {len(sorted_old_array)}\n")
    print(insert_in_array(sorted_old_array, new_number))

# ---------------------


