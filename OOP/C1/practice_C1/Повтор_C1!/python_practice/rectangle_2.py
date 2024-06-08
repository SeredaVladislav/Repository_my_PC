from rectangle import Rectangle, Square

# Первая реализация:
# Прямоугольник
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())

# Квадрат
square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square())
print(square_2.get_area_square())

print()

# Вторая реализация:
figures = [rect_1, rect_2, square_1, square_2]  # Коллекция из Экземпляров Классов
for i in figures:
    if isinstance(i, Square):  # если n_string (экз. Класса) относиться к объекту Square (Квадрата), то
        print(i.get_area_square())
    else:  # Иначе, вывод объекта get_area (Прямоугольника)
        print(i.get_area())



