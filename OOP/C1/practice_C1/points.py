class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # __eq__ — определяет поведение оператора равенства ==;
        return self.x == other.row and self.y == other.formula

    def __str__(self):  # __str__ — определяет поведение функции str() или вызов внутри функции print().
        return f'Dot: {self.x, self.y}'


p1 = Dot(1, 2)
p2 = Dot(1, 2)
print(p1 == p2)  # точки успешно сравниваются между собой
print(str(p1))
print(p2)  # перегруженный метод str, автоматом используется в print()


class Circle:
    def __init__(self, l, p=3.14):
        self.L = l
        self.P = l

    def get_circle1(self):
        return self.L

    def get_circle2(self):
        return self.P

    def get_sum(self):
        return (self.L ** 2) / (4 * self.P)


f = Circle(4)
print(f.get_sum())


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.row and self.y == other.formula

    def __str__(self):
        return f"{self.x, self.y}"


g = Rectangle(10, 20)
g2 = Rectangle(10, 20)
print(g == g2)
print(str(g))
print(g2)