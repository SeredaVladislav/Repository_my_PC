# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ str (Строки) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# НЕизменяемый;
# Хэшируемый;
# Последовательный;
# Итерируемый.


string: str = 'Привет'  # Одинарный апостроф;
string_2: str = '''Привет'''  # тройной апостроф;
string_3: str = "Привет"  # кавычки;
string_4: str = """Привет"""  # тройные кавычки.

# Индексы:
print(string[0])  # нулевой (первый символ) элемент 'П';
print(string[4])  # четвёртый (пятый символ) элемент 'е';
print(string[-1])  # последний элемент 'т'.
# Срезы:
print(string[1:4])  # с первого по четвертый (не вкл.) элементы 'рив';
print(string[2:])  # со второго элемента и до конца строки 'ивет';
print(string[:4])  # с начала строки и до четвертого элемента 'Прив';
print(string[::2])  # от начала и до конца строки, с шагом "два" 'Пие';
print(string[::-1])  # реверс строки 'тевирП';
print(string[-3:-1])  # от третьего (с конца) элемента до последнего 'ве'.


# Методы для str: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Все используемые методы для str которые преобразуют строку, возвращают новую строку, исходная остается
# неизменной (т.к. str НЕизменяемый тип данных).


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .join()
# Метод собирает строку из элементов списка, используя в качестве разделителя строку, к которой применяется метод.

def greet(name, *args):
    return " ".join((name,) + args)


print(greet('Timur', 'Roman', 'Ruslan'))

# Соединяет элементы из list с разбитием по ' ', преобразовывая в str:
words: list[str] = ['Python', 'is', 'the', 'most', 'powerful', 'language']
new_words = ' '.join(words)
print(new_words)  # Python is the most powerful language

# Соединяет элементы из list с переносом на другую строку, преобразовывая в str:
words_2: list[str] = ['a', 'b', 'c', 'd']
new_words_2 = "\n".join(words_2)
print(new_words_2)
# a
# b
# c
# d


# Разделение каждого элемента строки из list указанным символом:
words_3: list[str] = ['Мы', 'учим', 'язык', 'Python']
print('*'.join(words_3))  # Мы*учим*язык*Python
print('-'.join(words_3))  # Мы-учим-язык-Python

# Разделение каждого элемента строки, символом из переменной str_separator:
text: str = input()  # text
separator: str = input()  # **
print(separator.join(text))  # t**e**x**t

# Удалить все знаки из строки, с помощью .join():
sentence = '''
My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a 
pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if 
you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know 
those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed 
by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.
'''

symbols = [".", ",", ";", ":", "(", ")"]
array_not_symbols = "".join(word for word in sentence if word not in symbols)

print(*array_not_symbols.split())
# My very photogenic mother died in a freak accident picnic lightning when I was three and save for a
# pocket of warmth in the darkest past nothing of her subsists within the hollows and dells of memory over which if
# you can still stand my style I am writing under observation the sun of my infancy had set surely you all know
# those redolent remnants of day suspended with the midges about some hedge in bloom or suddenly entered and traversed
# by the rambler at the bottom of a hill in the summer dusk a furry warmth golden midges

# Удалить все буквы, оставив только числа
string_ = '10abc20de30pop5 5 5 5'
del_words = "".join([i if i.isdigit() else " " for i in string_]).split()

print(list(map(int, del_words)))
# [10, 20, 30, 5, 5, 5, 5]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Методы .upper(), .lower(), .swapcase(), .capitalize(), .title()
# Методы выполняют преобразование регистра строки.

words_4: str = 'python - Язык ПрограММирования'

# Преобразование в верхний регистр:
example_words_4_1 = words_4.upper()
print(example_words_4_1)  # 'PYTHON - ЯЗЫК ПРОГРАММИРОВАНИЯ'

# Преобразование в нижний регистр:
example_words_4_2 = words_4.lower()
print(example_words_4_2)  # 'python - язык программирования'

# Преобразование из верхнего в нижний регистр и наоборот:
example_words_4_3 = words_4.swapcase()
print(example_words_4_3)  # 'PYTHON - яЗЫК пРОГРАммИРОВАНИЯ'

# Преобразование в нижний регистр, а первую в верхний:
example_words_4_4 = words_4.capitalize()
print(example_words_4_4)  # 'Python - язык программирования'

# Преобразование в нижний регистр, а первую букву каждого слова в верхний:
example_words_4_5 = words_4.title()  # 'Python - Язык Программирования'
print(example_words_4_5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .isspace()
# Состоит ли строка из неотображаемых символов:
# "пробел" - ' ';
# "горизонтальная табуляция" - '\t';
# "вертикальная табуляция" - '\v';
# "перевод на новую строку" - '\n'.

example: str = "  "
print(example.isspace())  # True
example_2 = "Hello    Boy"
print(example_2.isspace())  # False
example_3 = "\n\n\t\n\n"
print(example_3.isspace())  # True
example_4 = "HelloGirl"
print(example_4.isspace())  # False

# Проверка, содержат ли переменные только неотображаемые символы:
example_5 = "  "
example_6 = "\t"
if example_5.isspace() and example_6.isspace():
    print("YES")  # YES
else:
    print("NO")

# Проверка, количества вхождений в строку неотображаемых символов:
example_7 = 'KGF movie starring\n\n\n\n\n\n Yash'
count = 0
for symbol in string:
    if symbol.isspace():
        count += 1
print(count)  # 9

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Методы .isdigit(), .isalpha(), .isalnum(), .islower(), .isupper(), .istitle()

words_5 = "Привет, мне 15 лет!"

# Состоит ли строка только из цифр:
print(words_5.isdigit())

# Состоит ли строка только из букв:
print(words_5.isalpha())

# Состоит ли строка из цифр или букв:
print(words_5.isalnum())

# Состоит ли строка только из символов в нижнем регистре:
print(words_5.islower())

# Состоит ли строка только из символов в верхнем регистре:
print(words_5.isupper())

# Начинается ли строка с заглавной буквы:
print(words_5.istitle())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .count()
# Метод используется для подсчета того, сколько раз символ или подстрока встречаются в строке.

words_6: str = 'Hello, hello, hello, hello'

print(words_6.count('hello'))  # 3
print(words_6.count('ello'))  # 4
print(words_6.count('l'))  # 8

# Необязательные аргументы у метода, позволяют указать длину списка по которому будет поиск вхождений:
print(words_6.count('l', 0, 8))  # 2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .find(), .rfind()
# Методы возвращают индекс первого .find() или последнего .rfind() вхождения в строку, передавая в качестве
# аргумента подстроку или символ. Если аргумент не найден, то возвращает -1.

words_7 = 'interface FastEthernet0/1'
print(words_7.find('Fast'))  # 10

words_7 = 'interface FastEthernet0/1'
print(words_7.rfind('n'))  # 19

# Срез с указанием найденного индекса через метод .find():
print(words_7[words_7.find('Fast')::])
# 'FastEthernet0/1'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Методы row(), rindex()
# Метод .row() идентичен методу .find(), за тем исключением, что он вызывает ошибку ValueError во время выполнения
# программы, если подстрока <sub> не найдена.

# Метод .rindex() идентичен методу .rfind(), за тем исключением, что он ищет первое вхождение подстроки
# начиная с конца строки, или возвращает ошибку ValueError.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Методы .startswith(), .endswith()
# Метод проверяет, начинается .startswith() или заканчивается .endswith() ли строка на определенные символы:

words_8 = 'Привет пёс!'

print(words_8.startswith('При'))  # True
print(words_8.startswith('т'))  # False

print(words_8.endswith('пёс!'))  # True
print(words_8.endswith('вет'))  # False

# Методам можно передавать несколько значений (обязательно как кортеж):
chk = "test".startswith(("d", "t"))
print(chk)  # True

chk = "test".startswith(("r", "a"))
print(chk)  # False

chk = "rtest".startswith(("r", "a"))
print(chk)  # True

chk = "rtest".endswith(("r", "a"))
print(chk)  # False

chk = "rtest".endswith(("r", "t"))
print(chk)  # True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .replace()

words_9 = 'Привет пёс!'.replace("ё", "Ы", 5)
# old - подстрока или символ который меняем;
# new - подстрока или символ на который меняем;
# count - сколько раз меняем;
print(words_9)

ar = "hello Mic, age 12"
print(list(map(str, ar.replace(' ', '!').split())))
# ['hello!Mic,!age!12']

# Замена последовательности символов в строке на другую последовательность:
string1 = 'FastEthernet0/1'
print(string1.replace('Fast', 'Gigabit'))  # 'GigabitEthernet0/1'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .strip(), .lstrip(), .rstrip()
# Методы убирает пробельные символы из строки.
# В набор символов входят: \t\n\r\f\v.

# По умолчанию метод .strip() убирает пробелы из начала и конца строки:
words_10 = '      interface FastEthernet0/1     '
print(words_10.strip())
# 'interface FastEthernet0/1'

# Методу .strip('str') можно передать как аргумент любые символы.
# Тогда в начале и в конце строки будут удалены все символы, которые были указаны в аргументе:

words_11 = '[110/1045]'
print(words_11.strip('[5]'))  # 110/104

# Если необходимо убрать символы только слева или только справа, можно использовать,
# соответственно, методы str.lstrip() и str.rstrip().

# Удалить все знаки из строки, с помощью str.strip():
sentence = '''
My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a 
pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if 
you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know 
those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed 
by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.
'''

symbols = ".,;:()"
array_not_symbols = [word.strip(symbols) for word in sentence.split()]

print(*array_not_symbols)
# My very photogenic mother died in a freak accident picnic lightning when I was three and save for a
# pocket of warmth in the darkest past nothing of her subsists within the hollows and dells of memory over which if
# you can still stand my style I am writing under observation the sun of my infancy had set surely you all know
# those redolent remnants of day suspended with the midges about some hedge in bloom or suddenly entered and traversed
# by the rambler at the bottom of a hill in the summer dusk a furry warmth golden midges


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Методы .ljust(), .rjust()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод .split()
# Метод разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов,
# преобразуя строку в list строк:

# Разбивает строку по пробелам и возвращает список строк:
words_12 = 'Python is the most powerful language'
words_12 = words_12.split()
print(words_12)  # ['Python', 'is', 'the', 'most', 'powerful', 'language']

# Преобразование списка в строку:
words_13 = [80, 443, 8080, 8081]
print(str(words_13).strip('[]'))  # 80, 443, 8080, 8081

# Необязательный параметр указывает разделитель:
words_14 = '192.168.1.24'
example_list_10 = words_14.split('.')
print(example_list_10)  # ['192', '168', '1', '24']

words_15 = 'Python    is   the  most  powerful  language'
example_words_15 = words_15.split()
example_words_16 = words_15.split(' ')
print(example_words_15)  # ['Python', 'is', 'the', 'most', 'powerful', 'language']
print(example_words_16)  # ['Python', '', '', '', 'is', '', '', 'the', '', 'most', '', 'powerful', '', 'language']

words_17 = "У лукоморья дуб зеленый златая цепь на дубе том".split()
print(*words_17, sep="\n")
# У
# лукоморья
# дуб
# зеленый
# златая
# цепь
# на
# дубе
# том

# Разбивает строку по \ и выводит по отдельности каждый элемент строки:
words_18 = "C:\Windows\System32\calc.exe".split('\\')
for i in words_18:
    print(i)
# C:
# Windows
# System32
# calc.exe

# Разбитие строки по "." с выводом list из строк:
words_19: list = input().split(".")

# Перебор всех индексов списка на предмет нахождения их в диапазоне:
x: bool = all(0 <= int(i) < 255 for i in words_19)
if x is False:
    print("НЕТ")
else:
    print("ДА")

# Ввод чисел через пробел:
str_numbers: list = list(map(int, input().split()))  # 1 7 5 7 5
print(str_numbers)  # [1, 7, 5, 7, 5]

# Ввод без пробела:
str_numbers: list = list(map(int, input()))  # 17575
print(str_numbers)  # [1, 7, 5, 7, 5]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Метод partition()
# Метод принимает на вход один аргумент sep, разделяет строку при первом появлении sep и возвращает
# кортеж, состоящий из трех элементов: часть перед разделителем, сам разделитель и часть после разделителя. Если
# разделитель не найден, то кортеж содержит саму строку, за которой следуют две пустые строки.

s1 = 'abc-de'.partition('-')
s2 = 'abc-de'.partition('.')
s3 = 'abc-de-fgh'.partition('-')

print(s1)  # ('abc', '-', 'de')
print(s2)  # ('abc-de', '', '')
print(s3)  # ('abc', '-', 'de-fgh')

# Преобразование строк: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

int_num = int(input("Введите целое число: "))
print(type(int_num))  # <class 'int'>

age = 25
my_age = "I'm " + str(age)
print(my_age)  # I'm 25

wow = 'wow'
print(wow * 5)  # wowwowwowwowwow

# Форматирование строк: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

age = 30
my_age = "I'm %d years old" % age
print(my_age)  # I'm 25 years old

# %d, %u, %i Целое число;
# %5d Выделяет пространство 5 символов под это число. Выравнивание вправо, остальное пространство остается пустым;
# %05d Выделяет пространство в 5 символов, но свободное пространство слева заполняется 0;
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# %o Число в восьмеричной системе счисления;
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# %x, %X Число в шестнадцатеричной системе счисления;
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# %g, G	Число с плавающей точкой;
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# %s Строка;
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# %% Если необходимо использовать просто как символ в строке.

day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2


# Форматирование строк 4 способа: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

name = 'Vlad'
age = 30

# Интерполяция строк / f-строки (Python v.3.6+)
print(f"Моё имя {name}. Мне {age} лет.")
# Форматирование строк через .format (Python v.3)
print("Моё имя {}. Мне {} лет.".format(name, age))
# Форматирование строк через % (Python до v.3)
print("Моё имя %s Мне %d лет." % (name, age))

# Конкатенация строк:
print("Моё имя " + name + ". Мне " + str(age) + " лет.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Конвертация int в 16-ную систему исчисления:
errno = 50159747054
print('%x' % errno)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Шаблонные строки (Стандартная библиотека Template Strings):

from string import Template

t = Template('Hey, $name!')
print(t.substitute(name=name))  # Вывод: 'Hey, Vlad!'

templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))
# Вывод: 'Hey Vlad, there is a 0xbadc0ffee error!'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Пример использования нужной команды, для доступа к закрытой части кода:
# Вот ваш супер-секретный ключ:
SECRET = 'Внутренняя информация! Не для пользователя'


class Error:
    def __init__(self):
        pass


# Злоумышленник может создать форматную строку, которая
# может считать данные из общего словаря:
user_input = input()

# Это позволяет ему профильтровать конфиденциальную информацию
# такую, как секретный ключ:
err = Error()
print(user_input.format(error=err))  # Вывод: 'this-is-a-secret'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from string import Template

# Правильный вариант решения:
print(Template(user_input).substitute(error=err))
