# ---------------------------------------------- Запись данных в файлы -------------------------------------------------
# -------------------------------
# ------------

# 'r' Read (чтение) Открыть файл только для чтения. Такой файл не может быть изменен.

# 'w' Write (запись) Открыть файл для записи. Если файл уже существует, то стереть его содержимое. Если файл не
# существует, он будет создан.

# 'a' Append (добавление) Открыть файл для записи. Все записываемые в файл данные будут добавлены в его конец. Если
# файл не существует, то он будет создан.

# 'r+' Read + Write	Открыть файл для чтения и записи. В этом режиме происходит частичная перезапись содержимого
# файла с самого начала.

# 'x' Create (создание)	Создать новый файл. Если файл уже существует, произойдет ошибка.
# ------------

# Для записи используются два файловых метода:
# 1. write() – записывает переданную строку в файл;
# 2. writelines() – записывает переданный список строк в файл.
# ------------


# -------------------------------
# Метод write():
# файловая_переменная.writе(строковое_значение):
# 1. Файловая переменная – это имя переменной, которая ссылается на файловый объект;
# 2. Строковое значение – это символьная последовательность, которая будет записана в файл.

# !!! Для записи данных в файл он должен быть открыт для записи (режимы 'w', 'а', 'r+'), иначе произойдет ошибка.

# ------------
# Пример: файл myfile.txt содержит:
# First line of the file.
# Second line of the file.
# Third line of the file.

# Для "w":
# Файл будет очищен и произойдет новая запись в файл:
with open('myfile.txt', 'w', encoding='utf-8') as file:
    file.write('Python and beegeek forever\n')
    file.write('We love stepik <3')
    # Python and beegeek forever
    # We love stepik <3

# Для "a":
# В конец файла будет добавлена новая информация:
with open('myfile.txt', 'a', encoding='utf-8') as file:
    file.write('Python and beegeek forever\n')
    file.write('We love stepik <3')
    # First line of the file.
    # Second line of the file.
    # Third line of the file.Python and beegeek forever
    # We love stepik <3

# Для "r+":
# С произойдет перезапись файла с начальной позиции:
with open('myfile.txt', 'r+', encoding='utf-8') as file:
    file.write('Python and beegeek forever\n')
    file.write('We love stepik.')
    # Python and beegeek forever
    # We love stepik. file.
    # Third line of the file.
# 2 новые строки запишутся в файл вместо первых 2-х уже имеющихся.

# -------------------------------
# Метод writelines():
# Метод writelines() принимает в качестве аргумента список строк и записывает его в файл.

philosophers = ['Джoн Локк\n', 'Дэвид Хьюм\n', 'Эдмyнд Берк\n']

with open('philosophers.txt', 'w', encoding='utf-8') as file:
    file.writelines(philosophers)

# !!! Оканчивающиеся строки имеющие экранированную последовательность '\n', будут записаны с новой строки!

# -------------------------------
# Запись в файл с помощью функции print():
# Для этого передается в функцию print() аргумент file, указывающий на открытый файл.
# !!! Функция print() автоматически добавляет переход на новую строку.

with open('philosophers.txt', 'w', encoding='utf-8') as output:
    print('Джoн Локк', file=output)
    print('Дэвид Хьюм', file=output)
    print('Эдмyнд Берк', file=output)
    # Джoн Локк
    # Дэвид Хьюм
    # Эдмyнд Берк

# Пример с форматированием выводимого текста:
with open('philosophers.txt', 'w', encoding='utf-8') as output:
    print('Джoн Локк', 'Дэвид Хьюм', 'Эдмyнд Берк', sep='***', file=output)
    # создает файл philosophers.txt с содержимым:
    # Джoн Локк***Дэвид Хьюм***Эдмyнд Берк

# ------------
with open('transliteration.txt', 'w') as output:
    print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
    print('python', file=output)
    # stepik*beegeek*iq-option+
    # python

# ------------
# Примечание:
# Данные сначала пишутся в буфер. Когда буфер заполняется, система записывает его содержимое в файл. Это увеличивает
# производительность системы, потому что запись данных в оперативную память быстрее записи на диск. Процесс закрытия
# файла записывает любые несохраненные данные из буфера в файл. Чтобы принудительно записать содержимое буфера в файл,
# используется файловый метод flush().

# ------------
with open('beegeek.txt', 'w') as file:
    file.writelines(['Добро пожаловать в Beegeek!\n', 'Наши курсы самые лучшие! '])
    file.write('Позвоните нам: (916) 928-92xx')
    # Добро пожаловать в Beegeek!
    # Наши курсы самые лучшие! Позвоните нам: (916) 928-92xx

# -------------------------------
# Задачи:

"""Напишите программу, которая считывает строку текста и записывает её в текстовый файл output_conc.txt."""
# Вариант 1:
with open('output.txt', 'w', encoding='UTF-8') as file:
    input_text = input()
    file.write(input_text)

# Вариант 2:
with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write(input())

# Вариант 3:
with open('output.txt', 'w', encoding='UTF-8') as file:
    input_text = input()
    print(input_text, file=file)
# ------------

from random import randint

with open('random.txt', 'a') as f:
    """
    Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел в диапазоне от 111 до 777 
    (включительно), каждое с новой строки.
    """
    for _ in range(25):
        f.write(f"{randint(111, 778)}\n")
# ------------

"""
    Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого 
    этого файла в файл output_conc.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и 
    пробел. Нумерация строк должна начинаться с 1.
"""

with open('input.txt') as in_f, open('output.txt', 'w') as out_f:
    [out_f.write(f'{i + 1}) {v}') for i, v in enumerate(in_f.readlines())]
# ------------

"""
    Сколько из них составляет более 7% от общего количества козлов?
    Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех 
    возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных 
    цветов. Перечень козлов включает только строки из первого списка.
    Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от 
    Жака Фреско.
"""
from decimal import Decimal as D

with open('goats.txt') as g_f, open('answer.txt', 'w') as ans_f:
    goats = "".join(g_f.read().split('GOATS')[1]).strip().split('\n')

    d_col = dict()
    total_num = len(goats)

    for key in goats[1::]:
        d_col[key] = goats.count(key)

    print(*sorted(filter(lambda x: x if D(str(d_col[x])) / D(str(total_num)) * 100 > 7 else None, d_col)), sep='\n',
          file=ans_f)
# ------------

"""
    На вход программе подается натуральное число n и n строк с названиями файлов. Напишите программу, которая 
    создает файл output_conc.txt и выводит в него содержимое всех файлов, не меняя их порядка. Смотрите Примечание 2 для 
    понимания работы программы.
    Примечание 2. Если бы на вход было подано 2 файла и эти файлы содержали бы строки (обратите внимание, что в конце 
    первого файла нет переноса строки)
"""

with open('output_conc.txt', 'w') as output:
    name_files = [input() for _ in range(int(input()))]

    for name in name_files:
        with open(name) as reading_files:
            output.write(reading_files.read())
# ------------

"""
    Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее.
    Каждая строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа,
    время выхода, где время указано в 24-часовом формате. Напишите программу, которая создает файл output_log.txt и
    записывает в него имена всех пользователей (не меняя порядка следования), которые были в сети не менее часа.
"""

from datetime import datetime as dt, timedelta as delta

with open('logfile.txt') as log_f, open('output_log.txt', 'w') as out_f:
    for line in log_f.readlines():
        line = line.strip().split(', ')

        if dt.strptime(line[2], '%H:%M') - dt.strptime(line[1], '%H:%M') >= delta(minutes=60):
            print(line[0], file=out_f)
# ------------

