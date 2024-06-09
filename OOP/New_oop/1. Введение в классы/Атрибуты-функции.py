# -------------------------------------------------- Атрибуты-функции --------------------------------------------------
# -------------------------------
# ------------

# Кроме атрибутов в виде переменных класса, так же применяются функции:
class Car:
    model = "BMW"
    engine = 1.6

    def drive():
        print("Let's go")


print(Car.__dict__)


# {'__module__': '__main__', 'model': 'BMW', 'engine': 1.6, 'drive': <function Car.drive at 0x7fcdf9f00670>,
# '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>,
# '__doc__': None}

# Для вызова атрибута-функцию:
# 1. class_name.attribute_function_name(), где class_name — имя класса, а attribute_function_name — имя атрибута.
# 2. getattr(class_name, 'attribute_name')()

class Car:
    model = "BMW"
    engine = 1.6

    def drive():
        print("Let's go")


Car.drive()  # Let's go
getattr(Car, 'drive')()  # Let's go


# P.S. Обращение напрямую к атрибуту-функции через экземпляр класса невозможно.

# -------------------------------
# Вызвать атрибут-функцию через экземпляр класса можно использовав декоратор @staticmethod:
class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod
    def drive():
        print("Let's go")


a = Car()
b = Car()
Car.drive()  # Let's go
getattr(Car, 'drive')()  # Let's go
a.drive()  # Let's go
b.drive()  # Let's go
