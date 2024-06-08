# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ float (Вещественные числа) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Примеры использования преобразования объектов к типу float:

# # Преобразование типа int к типу float
float(10)  # 10.0

# Преобразование строки с записью числа в тип float:
float(' -15  ')  # -15.0
float(' -15_125')  # -15125.0
float('  -3.500 ')  # -3.5
float('.500  ')  # 0.5
float(' -1e-1')  # -0.1
float('  1.e-5 ')  # 1e-05
float('  1.5e7 ')  # 15000000.0
float('  3.5657e+3 ')  # 3565.7
float('nan')  # nan
float('-inf')  # -inf
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Числа с плавающей точкой поддерживают следующие операции:
# 1. Арифметические операции;
# 2. Операции сравнения.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Методы типа float:

# Метод float.as_integer_ratio()
# Метод возвращает кортеж целых чисел, первое из которых равно числителю, а второе всегда положительному знаменателю
# дроби, значение которой точно равно исходному числу типа float:
# Новое в Python 3.8

3.5.as_integer_ratio()  # (7, 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Метод float.is_integer()
# Метод возвращает True если дробная часть числа равна 0 и False если нет:

3.0.is_integer()  # True
3.5.is_integer()  # False
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Метод float.hex()
# Метод возвращает представление числа в шестнадцатеричной системе счисления:

3.543212.hex()  # '0x1.c587f88765ba7p+1'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Метод float.fromhex(s):
# Метод преобразовывает шестнадцатеричную строку s в число типа float:

float.fromhex('0x1.9e00000000000p+6')  # 103.5
float.fromhex('   0x1.c587f88765ba7p+1    ')  # 3.543212
float.fromhex('   0x0.1p+3')  # 0.5
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
