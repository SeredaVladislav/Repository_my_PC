# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Дерево стандартных исключений ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# BaseException
#  +-- SystemExit (Исключение. Завершение работы кода)
#  +-- KeyboardInterrupt (Исключение. Нажатие клавиши прерывания)
#  +-- GeneratorExit (Исключение. Закрытие генератора)
#  +-- Exception
#   	+-- StopIteration
#   	+-- StopAsyncIteration
#   	+-- ArithmeticError
#   	|	FloatingPointError
#   	|	OverflowError
#   	|	ZeroDivisionError
#   	+-- AssertionError
#   	+-- AttributeError
#   	+-- BufferError
#   	+-- EOFError
#   	+-- ImportError
#   	|	+-- ModuleNotFoundError
#   	+-- LookupError
#   	|	+-- IndexError
#   	|	+-- KeyError
#   	+-- MemoryError
#   	+-- NameError
#   	|	+-- UnboundLocalError
#   	+-- OSError
#   	|	+-- BlockingIOError
#   	|	+-- ChildProcessError
#   	|	+-- ConnectionError
#   	|	|	+-- BrokenPipeError
#   	|	|	+-- ConnectionAbortedError
#   	|	|	+-- ConnectionRefusedError
#   	|	|	+-- ConnectionResetError
#   	|	+-- FileExistsError
#   	|	+-- FileNotFoundError
#   	|	+-- InterruptedError
#   	|	+-- IsADirectoryError
#   	|	+-- NotADirectoryError
#   	|	+-- PermissionError
#   	|	+-- ProcessLookupError
#   	|	+-- TimeoutError
#   	+-- ReferenceError
#   	+-- RuntimeError
#   	|	+-- NotImplementedError
#   	|	+-- RecursionError
#   	+-- SyntaxError
#   	|	+-- IndentationError
#   	|     	+-- TabError
#   	+-- SystemError
#   	+-- TypeError
#   	+-- ValueError
#   	|	+-- UnicodeError
#   	|     	+-- UnicodeDecodeError
#   	|     	+-- UnicodeEncodeError
#   	|     	+-- UnicodeTranslateError
#   	+-- Warning
#        	+-- DeprecationWarning
#        	+-- PendingDeprecationWarning
#        	+-- RuntimeWarning
#        	+-- SyntaxWarning
#        	+-- UserWarning
#        	+-- FutureWarning
#        	+-- ImportWarning
#        	+-- UnicodeWarning
#        	+-- BytesWarning
#        	+-- ResourceWarning

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# try:
# код, который может вызвать ту или иную ошибку

# except:
# код, который выполнится в случае возникновения ошибки

# else:
# код, который выполнится только в случае если в try ничего не сломалось

# finally:
# код, который выполнится в любом случае

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

try:
    raise ZeroDivisionError  # возбуждаем исключение ZeroDivisionError
except ArithmeticError:  # ловим его родителя
    print("Hello from arithmetic error")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Zero division error")
except ArithmeticError:
    print("Arithmetic error")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Собственные исключения: (Наследование от класса Exception обязательно!)

class MyException(Exception):  # создаём пустой класс – исключения
    pass


try:
    raise MyException("message")  # поднимаем наше исключение
except MyException as e:  # ловим его
    print(e)  # выводим информацию об исключении


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Наследования собственных исключений:

class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
    pass


class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуем от ParentException
    pass


try:
    raise ChildException("message")  # поднимаем исключение-наследник
except ParentException as e:  # ловим его родителя
    print(e)  # выводим информацию об исключении


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Дополнение к классу исключений:

class ParentException(Exception):
    def __init__(self, message,
                 error):  # допишем к нашему пустому классу конструктор, который будет печатать дополнительно
        # в консоль информацию об ошибке.
        super().__init__(message)  # помним про вызов конструктора родительского класса
        print(f"Errors: {error}")  # печатаем ошибку


class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    def __init__(self, message, error):
        super().__init__(message, error)


try:
    raise ChildException("message", "error")  # поднимаем исключение-наследник, передаём
    # дополнительный аргумент
except ParentException as e:
    print(e)  # выводим информацию об исключении


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Пример:

class NonPositiveDigitException(ValueError):
    """Созданный класс исключения, унаследованный от класса из дерева исключений"""
    pass


class Square:
    def __init__(self):
        self._a = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise NonPositiveDigitException('Сторона квадрата должна быть положительным числом!')
        self._a = value

    def set_s(self, aa):
        self.a = aa
        return self.a


f = Square()
print(f.set_s(-5))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Пример:

ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-"
ALPHABET_UPPER = ALPHABET.upper()

passport = input()

if passport is type(str):
    raise TypeError("Ввод должен быть строкой")

s_passport = passport.split()

if len(s_passport) != 2 or len(s_passport[0]) != 4 or len(s_passport[1]) != 6:
    raise TypeError("Строка должна быть разделена пробелом")

for x in s_passport:
    if not x.isdigit():
        raise TypeError("В строке должны быть только числа")

print(passport)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fio = input()

letters = ALPHABET + ALPHABET_UPPER

f = fio.split()

if len(f) != 3:
    raise TypeError("Неверный формат. Если у Вас нет отчества введите '-'")

for s_fio in f:

    if len(s_fio.strip(letters)) != 0:  # если в данных содержатся разрешенные символы, метод strip() их удалит
        # и длина строки должна составить 0, если длина не равняется 0, то введены не разрешенные символы.

        raise TypeError("Используйте только кириллические буквы или тире '-' ")

print(fio)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
