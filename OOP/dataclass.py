# Использование @dataclass в Python полезно в ряде сценариев, где вам нужно создать класс для хранения данных.
# Вот несколько конкретных случаев, когда стоит рассмотреть использование @dataclass:

# 1. Простые классы для хранения данных
# Если ваш класс в основном предназначен для хранения данных и имеет мало (или вообще не имеет) логики,
# @dataclass значительно упростит код:
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


# 2. Автоматическое создание стандартных методов
# Если вам нужны методы __init__, __repr__, __eq__ и другие, @dataclass автоматически их генерирует, экономя время
# и снижая вероятность ошибок:

@dataclass
class Employee:
    name: str
    id: int
    department: str


# 3. Улучшенная читаемость и поддержка кода
# Классы с @dataclass более читаемы и менее загромождены шаблонным кодом:

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float


# 4. Обработка неизменяемых данных
# Если данные должны быть неизменяемыми, @dataclass поддерживает параметр frozen, который делает экземпляры
# класса неизменяемыми:

@dataclass(frozen=True)
class Color:
    red: int
    green: int
    blue: int


# 5. Опциональные и дефолтные значения
# @dataclass легко позволяет устанавливать значения по умолчанию для полей:

@dataclass
class Person:
    name: str
    age: int = 0
    gender: str = "Не указан"


# 6. Вложенные структуры данных
# Если вы работаете со сложными вложенными структурами данных, @dataclass помогает поддерживать чистоту и структуру
# кода:

@dataclass
class Address:
    street: str
    city: str
    zipcode: str


@dataclass
class User:
    name: str
    address: Address


# 7. Оптимизация и проверка типов
# Использование @dataclass совместно с typing помогает улучшить проверку типов и автодополнение в IDE:

from typing import List


@dataclass
class Student:
    name: str
    grades: List[int]


# 8. Упрощение сериализации/десериализации
# Классы с @dataclass легко сериализовать и десериализовать в такие форматы, как JSON:
import json


@dataclass
class Product:
    id: int
    name: str
    price: float


product = Product(1, "Laptop", 999.99)
json_str = json.dumps(product.__dict__)
print(json_str)

# Примеры использования и преимущества:
# Прототипирование и быстрое создание моделей данных: Быстрое создание классов для тестирования и разработки.
# Четкая структура и документированность: Определение данных и их типов на одном месте.
# Легкость изменений и расширяемость: Легко добавлять и изменять поля без необходимости переписывать методы
# инициализации и сравнения.

# ----------------------------------------------------------
# Пример, в котором будем явно видеть, как генерируются методы __init__, __repr__ и __eq__ при использовании @dataclass,
# и сравним их с версией, где эти методы определены вручную.

# Пример с использованием @dataclass

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    gender: str

    def profile(self):
        print(f"Имя пользователя: {self.name}\nВозраст: {self.age}\nПол: {self.gender}")


# Создание объекта
user_1 = Person('Владислав', 31, 'Мужской')

# Автоматически сгенерированный __repr__
print(user_1)  # Это вызовет сгенерированный метод __repr__

# Автоматически сгенерированный __eq__
user_2 = Person('Владислав', 31, 'Мужской')
print(user_1 == user_2)  # Это вызовет сгенерированный метод __eq__


# Person(name='Владислав', age=31, gender='Мужской')
# True


# Пример без использования @dataclass, со всеми методами определенными вручную:
class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def profile(self):
        print(f"Имя пользователя: {self.name}\nВозраст: {self.age}\nПол: {self.gender}")

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age}, gender='{self.gender}')"

    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return (self.name, self.age, self.gender) == (other.name, other.age, other.gender)
        return False


# Создание объекта
user_1 = Person('Владислав', 31, 'Мужской')

# Явно определенный __repr__
print(user_1)

# Явно определенный __eq__
user_2 = Person('Владислав', 31, 'Мужской')
print(user_1 == user_2)
# Person(name='Владислав', age=31, gender='Мужской')
# True


# Объяснение:
# __init__:
# С @dataclass: Метод __init__ генерируется автоматически, инициализируя все поля, указанные в классе. Вы не видите его
# в коде, но он работает за кулисами.
# Без @dataclass: Метод __init__ нужно определить вручную, чтобы инициализировать поля объекта.

# __repr__:
# С @dataclass: Метод __repr__ генерируется автоматически и возвращает строку, которая содержит имя класса и значения
# всех его полей, что полезно для отладки.
# Без @dataclass: Метод __repr__ нужно определить вручную, чтобы получить аналогичный вывод.

# __eq__:
# С @dataclass: Метод __eq__ генерируется автоматически и сравнивает объекты на основе значений всех их полей.
# Без @dataclass: Метод __eq__ нужно определить вручную, чтобы обеспечить правильное сравнение объектов.
