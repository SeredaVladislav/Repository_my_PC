# --------------------------------------------- Декоратор property -----------------------------------------------------
# -------------------------------
# ------------

# Дескриптор - специальный протокол или интерфейс, который позволяет вам контролировать доступ к атрибутам объекта
# через методы __get__, __set__ и __delete__.


# Пример работы с функцией(классом) property, где создается свойство с описанием геттеров, сеттеров, билетеров:
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('Get balance')
        return self.__balance

    def set_balance(self, value):
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('Delete balance')
        del self.__balance

    my_balance = property(fget=get_balance,
                          fset=set_balance,
                          fdel=delete_balance)


if __name__ == '__main__':
    print()

# ------------

# У объекта property имеется 3 метода:
# .getter() позволяет определить геттер
# .setter() позволяет определить сеттер
# .deleter() позволяет определить делитер

# Результатом вызова каждого метода свойства будет новый экземпляр класса свойства.
# При помощи этих методов мы можем переписать определение свойства balance. Вот так оно было определенно ранее:

balance = property(fget=get_balance,
                   fset=set_balance,
                   fdel=delete_balance)

# и вот как будет описано через вызов методов:

balance = property()
balance = balance.getter(get_balance)
balance = balance.setter(set_balance)
balance = balance.deleter(delete_balance)

# Или в функцию property можно сразу передать геттер-функцию и тогда код станет еще короче:

balance = property(get_balance)
balance = balance.setter(set_balance)
balance = balance.deleter(delete_balance)


# Итоговый результат:
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('Get balance')
        return self.__balance

    def set_balance(self, value):
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('Delete balance')
        del self.__balance

    balance = property(get_balance)
    balance = balance.setter(set_balance)
    balance = balance.deleter(delete_balance)


# Теперь доступна работа через свойство, но доступ к методам тоже остается!
# -------------------------------

# --------------------------------------------- Геттер-свойство через декоратор ----------------------------------------
# Декораторы — это функции, которые принимают другую функцию в качестве аргумента, добавляют к ней некоторую
# дополнительную функциональность и возвращают функцию с измененным поведением.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def my_balance(self):  # метод
        print('Get balance')
        return self.__balance

    my_balance = property(my_balance)  # свойство


# Вариант с использованием синтаксического сахара:
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('Get balance')
        return self.__balance


# --------------------------------------------- Сеттер-свойство через декоратор ----------------------------------------

# После объявления геттер-свойства оно становится доступно внутри класса по своему имени, в нашем случае my_balance.
# Объект my_balance представляет собой свойство, а значит у него есть метод setter:

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('Get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value


# Главное, чтобы у метода сеттера было то же имя, что и у вашего свойства!!!

# --------------------------------------------- Делитер-свойство через декоратор ---------------------------------------

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('Get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('Set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('Delete balance')
        del self.__balance


# Имена всех наших методов имеют одинаковое название my_balance. Это нужно, чтобы функциональность геттера, сеттера и
# делитера находилась в одном свойстве  - my_balance.


# ------------------------------------------------------ Задачи --------------------------------------------------------

from dataclasses import dataclass


@dataclass
class Celsius:
    temp_value: int

    """
    Создайте класс Celsius, который представляет температуру в градусах Цельсия. Основная задача класса - предоставить
    возможность конвертировать температуру из градусов Цельсия в градусы Фаренгейта, а также обеспечить контроль за
    корректностью введенных значений.

    Класс Celsius, должен иметь:
    1. Метод __init__, который принимает значение температуры в градусах по Цельсию и сохраняет в атрибут экземпляра.
    2. Метод to_fahrenheit, который выполняет конвертацию температуры из градусов Цельсия в градусы Фаренгейта по
    формуле°F = (°C × 9/5) + 32 и возвращает результат этой конвертации.
    1. Свойство-геттер temperature, которое предоставляет доступ к значению температуры
    1. Свойство-сеттер temperature, которое выполняется при установке нового значения температуры. Если значение
    меньше -273.15 градусов Цельсия (абсолютный ноль), вызывается исключение ValueError. В противном случае, происходит
    установка нового значения температуры.
    """

    def to_fahrenheit(self):
        return (self.temp_value * 9 / 5) + 32

    @property
    def temperature(self):
        return self.temp_value

    @temperature.setter
    def temperature(self, new_value):
        if new_value < -273.51:
            raise ValueError("Температура ниже абсолютного нуля")
        self.temp_value = new_value


if __name__ == '__main__':
    celsius = Celsius(25)
    assert celsius.temperature == 25
    assert celsius.to_fahrenheit() == 77.0

    celsius.temperature = 30
    assert celsius.temperature == 30
    assert celsius.to_fahrenheit() == 86.0

    print('Good')


# -------------------------------
class File:
    """
    Создайте класс File, представляющий файл с указанным размером в байтах. Основная цель класса заключается в
    предоставлении удобного метода для преобразования размера файла из байтов в человеко-читаемые единицы измерения
    (Килобайты, Мегабайты, Гигабайты). Класс File, должен иметь:
    1. Метод __init__, который принимает размер файла в байтах как аргумент и инициализирует атрибут _size_in_bytes с
    этим значением.
    2. Свойство-геттер size, которое вычисляет и возвращает размер файла в удобной для чтения строковой форме. В
    зависимости от значения _size_in_bytes, метод форматирует вывод в байтах, килобайтах, мегабайтах или гигабайтах.

    Если размер меньше 1 КБ, выводится размер в байтах в формате "{значение} B".
    Если размер от 1 КБ до 1 МБ, выводится размер в килобайтах с двумя знаками после запятой в формате "{значение} KB".
    Если размер от 1 МБ до 1 ГБ, выводится размер в мегабайтах с двумя знаками после запятой в формате "{значение} MB".
    В противном случае (если размер больше 1 ГБ), выводится размер в гигабайтах с двумя знаками после запятой в формате
    "{значение} GB".
    3. Свойство-сеттер size, которое позволяет изменять значение атрибута _size_in_bytes
    """
    MEASURING_INFO = {1: " KB", 2: " MB", 3: " GB"}

    def __init__(self, size_in_bytes):
        self._size_in_bytes = size_in_bytes

    @property
    def size(self):
        value = self._size_in_bytes
        if value < 1024:
            return f"{value} B"
        else:
            count = 0
            while value > 10:
                count += 1
                value /= 1024
        return '%.2f' % round(value, 2) + self.MEASURING_INFO[count]

    @size.setter
    def size(self, value):
        self._size_in_bytes = value


if __name__ == '__main__':
    file = File(5)
    assert file.size == "5 B"
    file.size = 1023
    assert file.size == "1023 B"
    file.size = 1024
    assert file.size == "1.00 KB"

    file_1 = File(1500000)
    assert file_1._size_in_bytes == 1500000
    assert file_1.size == "1.43 MB"

    file_2 = File(1500)
    assert file_2.size == "1.46 KB"

    file_3 = File(2789326322)
    assert file_3.size == "2.60 GB"
    file_3.size = 1073741824
    assert file_3.size == "1.00 GB"

    print('Good')
