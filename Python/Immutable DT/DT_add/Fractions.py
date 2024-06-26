# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Модуль fractions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Рациональное число (Дробное) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Рациональное число – это число, которое можно представить в виде дроби n / m,
# где m числитель, n знаменатель, которые имеют целочисленное значение, при этом знаменатель не равен нулю.

# Знаменатель дроби показывает количество равных частей.
# Числитель дроби показывает, сколько из них взято.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Тип данных Fraction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Тип данных Fraction: (Immutable, Реализовано программно)

from fractions import Fraction

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Создание Fraction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Создать Fraction число можно несколькими способами:

# из целых чисел, передав значения числителя и знаменателя дроби,
# из строки на основании десятичного представления;
# из строки на основании обыкновенной дроби;
# из числа с плавающей точкой (не рекомендуется)

num1 = Fraction(3, 4)  # 3 - числитель, 4 - знаменатель
num2 = Fraction('0.55')
num3 = Fraction('1/9')
print(num1, num2, num3, sep='\n')
# 3/4
# 11/20
# 1/9

# --------------------
# Создание числа Fraction на основе float:
num = Fraction(0.34)
print(num)
# 6124895493223875/18014398509481984, ожидаемо 17/50

# --------------------
# При создании Fraction числа, дробь автоматически сокращается!
num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')
print(num1, num2, num3, sep='\n')
# 1/2
# 3/4
# 1/4

# --------------------
# Также стоит обратить внимание на вывод дробей, являющихся целыми числами.
num1 = Fraction(5, 1)  # 5/1 = 5
num2 = Fraction(23, 23)  # 23/23 = 1
print(num1, num2, sep='\n')
# 5
# 1


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Сравнение Fraction чисел ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Fraction числа можно сравнивать между собой точно так же, как и любые другие числа.

num1 = Fraction(1, 2)        # 1/2
num2 = Fraction(15, 30)      # 15/30=1/2
num3 = Fraction(3, 5)        # 3/5
num4 = Fraction(5, 3)        # 5/3
num5 = 1
num6 = 0.8

print(num1 == num2)
print(num1 != num4)
print(num2 > num3)
print(num4 <= num1)
print(num1 < num5)
print(num6 > num4)
# True
# True
# False
# False
# True
# False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Арифметические операции над Fraction числами~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

num1 = Fraction('1/10')
num2 = Fraction('2/3')
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
# 23/30
# -17/30
# 1/15
# 3/20

# --------------------
num = Fraction('3/8')
print(num + 1)
print(num - 1)
print(num * 2)
print(num ** 4)
# 11/8
# -5/8
# 3/4
# 81/4096


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Математические функции ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Fraction числа можно передавать как аргументы функций, ожидающих float. Тогда они будут преобразованы во float.
# К примеру, модуль math, оперирующий float числами, может работать и с Fraction числами.
from fractions import Fraction
from math import *

num1 = Fraction('1.44')
num2 = Fraction('0.523')

print(sqrt(num1))
print(sin(num2))
print(log(num1 + num2))
# 1.2
# 0.4994813555186418
# 0.6744739152943241
# Результат работы функции, число типа данных float

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Свойства numerator и denominator ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Для получения числителя и знаменателя Fraction числа используются свойства numerator и denominator.

num = Fraction('5/16')
print('Числитель дроби равен:', num.numerator)
print('Знаменатель дроби равен:', num.denominator)
# Числитель дроби равен: 5
# Знаменатель дроби равен: 16

# --------------------
num = Fraction('-5/16')
print(num.as_integer_ratio())  # Возвращает кортеж из числителя и знаменателя.
# (-5, 16)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Метод limit_denominator() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь, чей знаменатель не превосходит
# переданного аргумента.

from fractions import Fraction
import math

print('PI =', math.pi)

num = Fraction(str(math.pi))
print('No limit =', num)

for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)

# PI = 3.141592653589793
# No limit = 3141592653589793/1000000000000000
# 3
# 16/5
# 22/7
# 267/85
# 311/99
# 355/113
# 3126535/995207

# Метод limit_denominator() позволяет получить очень точные рациональные приближения иррациональных чисел, что очень
# удобно во многих математических задачах.































