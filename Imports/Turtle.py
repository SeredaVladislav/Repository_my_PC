# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Модуль turtle ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import turtle

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Движение ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ВСЕ НАСТРОЙКИ:
_CFG = {"width": 0.5,  # Screen
        "height": 0.75,
        "canvwidth": 400,
        "canvheight": 300,
        "leftright": None,
        "topbottom": None,
        "mode": "standard",  # TurtleScreen
        "colormode": 1.0,
        "delay": 10,
        "undobuffersize": 1000,  # RawTurtle
        "shape": "classic",
        "pencolor": "black",
        "fillcolor": "black",
        "resizemode": "noresize",
        "visible": True,
        "language": "english",  # docstrings
        "exampleturtle": "turtle",
        "examplescreen": "screen",
        "title": "Python Turtle Graphics",
        "using_IDLE": False
        }
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Прямая линия ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Отображения графического окна:
turtle.showturtle()

# ---------------------
# Команда turtle.Screen().setup() установка размера окна. Аргументы - (int, int). Размер окна в пикселях.

# ---------------------
# 1. Указатель в окне расположен в центре и направлен на восток (вправо).
# 2. При вводе команды двигаться вперед, указатель переместиться в направлении указываемом указателем.

# ---------------------
# Перемещение вперед на кол-во пикселей:
turtle.forward(100)

# ---------------------
# Перемещение назад на кол-во пикселей:
turtle.backward(250)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Поворот ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Ориентация в пространстве:
# 1. По-умолчанию (указатель вправо) == 0 градусов.
# 2. Противоположная сторона == 180 градусов.
# 3. Прямо вверх == 90 градусов.
# 4. Прямо вниз == 270 градусов.

# ---------------------
# turtle.right(angle) и turtle.left(angle) - повороты указателя на кол-во градусов.
turtle.right(90)
turtle.left(120)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Угол направления ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Чистый угол поворота, от опорной в 0 градусов:

# Команда turtle.setheading() применяется для установки углового направления указателя с заданным углом.
# В качестве аргумента нужно указать желаемый угол.

# Первоначальное угловое направление указателя составляет 0. Далее установлено направление указателя 90 (на север).
# Затем установлено направление указателя 180 (на запад). Потом установлено направление указателя 270 (на юг).

# Квадрат:
turtle.setheading(180)
# ---------------------
# Получение текущего углового направления указателя:
# Используется команда turtle.heading().
turtle.setheading(180)
print(turtle.heading())  # 180.0
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Перемещение в заданную позицию ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Команды turtle.setposition() и turtle.setpos() аналогичны команде turtle.goto().

# Все три команды перемещают черепашку в заданную позицию:
turtle.goto(0, 100)
turtle.goto(-100, 0)
turtle.goto(0, 0)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Получение текущей позиции ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Команда turtle.pos() возвращает кортеж с x и y координатами указателя:
turtle.goto(100, 150)
position = turtle.pos()  # (100.00,150.00)
print(position)

# Для координат по отдельности:
turtle.goto(200, -150)
x = turtle.xcor()  # для x
y = turtle.ycor()  # для y
print(x)  # 200
print(y)  # -150

# P.S. Команда turtle.position() аналогична команде turtle.pos(). Обе команды возвращают кортеж с x и y координатами.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Управление скоростью анимации ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Для изменения скорости движения черепашки можно применить команду turtle.speed().
# Аргумент команды скорость – число в диапазоне от 0 до 10.
# Если указать 0, то черепашка будет делать все свои перемещения мгновенно (анимация отключена):
turtle.speed(0)
turtle.circle(50)

# В диапазоне от 1 до 10 самая малая скорость – 1, а самая большая – 10.
for i in range(1, 11):
    turtle.speed(i)
    turtle.circle(100 - 10 * i)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Внешний вид ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Указатель ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# По умолчанию указатель выглядит как стрелка, но возможен и другой внешний вид. Для его изменения используют
# команду shape():

# Доступные фигуры:

# square (квадрат);
# arrow (стрелка);
# circle (круг);
# turtle (черепаха);
# triangle (треугольник);
# classic (классическая стрелка. По-умолчанию).

turtle.shape('square')
turtle.forward(100)
turtle.setheading(90)

turtle.shape('arrow')
turtle.forward(100)
turtle.setheading(180)

turtle.shape('turtle')
turtle.forward(100)
turtle.setheading(270)

turtle.shape('circle')
turtle.forward(100)
# ---------------------
# Замена указателя, на gif-изображение.

# Регистрация изображения:
turtle.Screen().addshape('34c44b321268000b8f7a1982365d40b9.gif')
# Добавление изображения: (Размещение изображения в директории файла!)
turtle.shape('34c44b321268000b8f7a1982365d40b9.gif')


def turtles():
    for _ in range(4):
        turtle.forward(250)
        turtle.left(90)


if __name__ == '__main__':
    turtles()

# ---------------------
# Вывод размеров холста в пикселях:
print(f"Размер холста:\n{turtle.window_width()}x{turtle.window_height()}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Сокрытие указателя ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Скрыть указатель:
turtle.hideturtle()  # либо,
turtle.ht()

# Отменить скрытие указателя:
turtle.showturtle()  # либо,
turtle.st()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Перо ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Команда turtle.penup() поднимает перо, а turtle.pendown() - опускает.
turtle.penup()
turtle.pendown()
# ---------------------
# Команда pensize() устанавливает ширину пера. Аргумент - толщина.
turtle.pensize(10)
# ---------------------
# Команда pencolor('red') устанавливает цвет пера. Аргумент - цвет(eng)
turtle.pencolor('red')

# P.S. Команда turtle.pencolor() позволяет работать не только с предопределенными названиями цветов, но и с цветами,
# заданными в формате RGB (Red Green Blue). В качестве аргумента команды turtle.pencolor() можно использовать либо
# кортеж из 3 чисел (r, g, b), либо просто три числа r, g, b.

# ВАЖНО! Чтобы использовать цвет в формате RGB, нужно предварительно установить значение colormode в 255, для этого
# нужно использовать команду turtle.Screen().colormode(255).

turtle.pencolor('red')  # строковое представление цвета

color = (13, 56, 240)  # кортеж (r, g, b)

turtle.pencolor(color)  # кортеж в качестве аргумента

turtle.pencolor(130, 240, 200)  # значения r, g, b в качестве аргументов
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Фон ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Команда turtle.Screen().bgcolor() для изменения фона окна, аргумент - цвет(eng или RGB)
turtle.Screen().bgcolor('gray')
# ---------------------
# Команда turtle.Screen().bgpic() для изменения фона с помощью изображения.
turtle.Screen().bgpic('space.jpg')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Круги и точки ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Команда turtle.circle() для рисунка круга, аргумент - радиус круга.
turtle.circle(80)
# ---------------------
# Команда turtle.dot() рисует точку. Аргумент - размер точки(int).

# Рисунок 3-х точек на прямой, с расстоянием в 50 пикселей:
turtle.dot()
turtle.forward(50)

turtle.dot()
turtle.forward(50)

turtle.dot()
turtle.forward(50)

# ---------------------
# Команда turtle.stamp() оставляет штамп в виде указателя.
turtle.shape('arrow')

for i in range(3):
    turtle.forward(50)
    turtle.stamp()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Сброс ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Команда turtle.clear() стирает все рисунки в графическом окне. Но не меняет положение черепашки, цвет рисунка и цвет
# фона графического окна.

# Команда turtle.reset() стирает все рисунки, имеющиеся в графическом окне, задает черный цвет рисунка и возвращает
# черепашку в исходное положение в центре экрана. Эта команда не переустанавливает цвет фона графического окна.

# Команда turtle.clearscreen() стирает все рисунки в графическом окне, меняет цвет рисунка на черный, а цвет фона на
# белый, и возвращает черепашку в исходное положение в центре графического окна.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Вывод текста в графическое окно ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import turtle

turtle.write('Пpивeт, мир!')  # выводит текст Привет, мир! на экран.

# Пример:
turtle.Screen().setup(400, 300)

turtle.hideturtle()  # Скрыть указатель
turtle.goto(-120, 120)
turtle.write('Сверху')
turtle.goto(50, -120)
turtle.write('Снизу')
turtle.goto(100, 20)
turtle.write('Справа')

# ---------------------
# Аргументы команды write():
# arg – текст, который нужно вывести;
# move – указывает, будет ли двигаться черепашка по мере рисования надписи (по умолчанию значение False);
# align – служит для выравнивания надписи относительно черепашки, может принимать три строковых значения right, center,
# left (по умолчанию значению right);
# font – кортеж из трех значений: (название шрифта, размер шрифта, тип начертания). В качестве начертания можно
# использовать строковые значения: normal — обычный, bold — полужирный, italic — курсив, или объединить два последних,
# тогда текст будет напечатан полужирным курсивом.
# ---------------------

import turtle

turtle.hideturtle()

turtle.goto(-120, 120)
turtle.write('Сверху', move=False, align='center', font=('Arial', 17, 'bold'))
turtle.goto(50, -120)
turtle.write('Снизу', move=True, align='left', font=('Times New Roman', 25, 'normal'))
turtle.goto(100, 20)
turtle.write('Справа', move=True, align='right', font=('Helvetica', 20, 'italic'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Заполнение геометрических фигур ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import turtle

turtle.hideturtle()
turtle.begin_fill()  # включаем заливку (она применяется до начертания фигуры)
turtle.circle(80)
turtle.end_fill()  # выключаем заливку
# ---------------------
# Цвет заливки можно изменить при помощи команды fillcolor(). Аргумент команды — название цвета в виде строкового
# литерала, либо значения трех компонентов RGB.

import turtle

turtle.hideturtle()

turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

# Пример:
import turtle

turtle.hideturtle()
turtle.fillcolor('green')

turtle.begin_fill()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()
# ---------------------
# Если заполнить незамкнутую фигуру, она будет закрашена, будто был начерчен отрезок, соединяющий начальную и
# конечную точки.
import turtle

turtle.hideturtle()
turtle.fillcolor('green')

turtle.begin_fill()

turtle.goto(-50, 120)
turtle.goto(120, 120)
turtle.goto(150, -80)

turtle.end_fill()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Создание нескольких черепашек ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Можно работать сразу с несколькими черепашками. Для этого надо создать несколько переменных, содержащих экземпляры
# класса Turtle.
import turtle

turtle.Screen().bgcolor('yellow')  # устанавливаем цвет фона

tim = turtle.Turtle()  # создаем первую черепашку и устанавливаем ее свойства
tim.color('red')
tim.pensize(3)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.right(180)
tim.forward(80)

alex = turtle.Turtle()  # создаем вторую черепашку и устанавливаем ее свойства
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
# ---------------------

# ---------------------
# ---------------------
# ---------------------
# Команда turtle.tracer(n, delay) включает/выключает анимацию черепашки и устанавливает задержку для обновления
# рисунков. Может использоваться для ускорения рисования сложной графики.
# ---------------------


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Отслеживание нажатия клавиш ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Черепашья графика позволяет отслеживать происходящие события, такие как нажатия клавиш клавиатуры, перемещение мышки
# или нажатие на мышку. Изначально программа никак не реагирует на эти события и чтобы это поведение изменить
# необходимо привязать функции обратного вызова к событиям. Для этого существуют специальные команды. Для отслеживания
# нажатия клавиш клавиатуры используется команда onkey(fun, key), которая связывает функцию обратного вызова fun с
# событием нажатия клавиши key.


import turtle


def move_up():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y + 5)


def move_down():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y - 5)


def move_left():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x - 5, y)


def move_right():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x + 5, y)


turtle.showturtle()  # отображаем черепашку
turtle.pensize(3)  # устанавливаем размер пера
turtle.shape('turtle')
turtle.Screen().listen()  # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо

# Для отслеживания событий также необходимо установить фокус на экран черепашки с помощью команды
# turtle.Screen().listen().
#
# Давайте теперь сделаем так, чтобы по нажатию на пробел черепашка скрывалась и переставала оставлять след. Также
# добавим возможность увеличивать скорость перемещения черепашки по нажатию на клавиши клавиатуры q и w.


import turtle

speed = 5


def move_up():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y + speed)


def move_down():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y - speed)


def move_left():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x - speed, y)


def move_right():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x + speed, y)


def change():  # функция обратного вызова
    if turtle.isvisible():
        turtle.up()
        turtle.hideturtle()
    else:
        turtle.down()
        turtle.showturtle()


def speed_increase():  # функция обратного вызова
    global speed
    speed += 1


def speed_decrease():  # функция обратного вызова
    global speed
    speed -= 1


turtle.showturtle()  # отображаем черепашку
turtle.pensize(3)  # устанавливаем размер пера
turtle.Screen().listen()  # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо
turtle.Screen().onkey(change, 'space')
turtle.Screen().onkey(speed_increase, 'q')
turtle.Screen().onkey(speed_decrease, 'w')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Отслеживание нажатия мыши ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Аналогичным образом можно отслеживать нажатие на мышку. Для отслеживания нажатия мыши используется команда
# onclick(fun), которая связывает функцию обратного вызова fun с событием нажатия левой кнопки мыши.

# Приведенный ниже код рисует круг по нажатию на левую кнопку мыши.

import turtle
from random import randrange


def random_color():
    return randrange(256), randrange(256), randrange(256)


def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    color = random_color()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.speed(0)


def left_mouse_click(x, y):
    draw_circle(x, y, 10)


turtle.hideturtle()

turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Задачи по модулю turtle:


import turtle as tr


def rectangle(width: int, height: int) -> None:
    """Напишите программу, которая рисует прямоугольник."""

    tr.forward(width)
    tr.left(90)
    tr.forward(height)
    tr.left(90)


if __name__ == '__main__':
    for _ in range(2):
        rectangle(100, 50)


# ---------------------
def triangle(side):
    """Напишите программу, которая рисует правильный треугольник."""
    tr.forward(side)
    tr.left(120)


if __name__ == '__main__':
    for _ in range(3):
        triangle(150)


# ---------------------
def square_3(side):
    """Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов."""

    tr.speed(100)

    tr.left(15)
    for _ in range(4):
        tr.forward(side)  # 150
        tr.left(90)

    tr.left(30)
    for _ in range(4):
        tr.forward(side)  # 150
        tr.left(90)

    tr.left(30)
    for _ in range(4):
        tr.forward(side)  # 150
        tr.left(90)


if __name__ == '__main__':
    square_3(150)


# ---------------------
def square_8(side):
    """Напишите программу, которая рисует изображенную фигуру из восьми квадратов."""

    flag = 0

    while flag < 8:
        for _ in range(4):
            tr.forward(side)
            tr.left(90)

        tr.left(45)
        flag += 1


square_8(250)


# ---------------------
def hexagon(side):
    """Напишите программу, которая рисует правильный шестиугольник."""
    for _ in range(6):
        tr.forward(side)
        tr.right(60)


hexagon(100)


# ---------------------
def hexagon(side):
    """Напишите программу, которая рисует соты."""
    tr.speed(3)

    for _ in range(6):
        tr.forward(side)
        tr.right(60)
        tr.forward(side)
        tr.back(side)
        tr.left(120)

    tr.right(120)
    tr.forward(side)

    for _ in range(6):
        for _ in range(3):
            tr.left(60)
            tr.forward(side)
        tr.right(120)


hexagon(100)

# ---------------------
"""Напишите программу, которая рисует ромб с углами 60 и 120 градусов."""
for x in [120, 60, 120, 60]:
    tr.forward(150)
    tr.left(x)


# ---------------------
def ten_diamonds(length):
    """Напишите программу, которая рисует снежинку из 10 ромбов."""

    ANGLE_DIA = [60, 120, 60, 120]
    tr.speed(speed_turtle)
    tr.width(width_line)
    tr.color(color_turtle)

    for _ in range(10):
        for i in ANGLE_DIA:
            tr.forward(length)
            tr.right(i)

        tr.right(36)


if __name__ == '__main__':
    speed_turtle, width_line, color_turtle = int(input("Скорость указателя: ")), int(input("Ширина линии: ")), input(
        "Цвет линии(eng): ")
    ten_diamonds(100)
    tr.done()


# ---------------------
def rays_of_stars(length_ray):
    """Напишите программу, которая рисует лучи звезды, показанной на рисунке."""
    tr.speed(5)
    tr.width(2)

    for _ in range(12):
        tr.forward(length_ray)
        tr.backward(length_ray)

        tr.left(30)


if __name__ == '__main__':
    rays_of_stars(200)


# ---------------------
def star(length):
    """Напишите программу, которая рисует правильную пятиконечную звезду."""
    tr.speed(5)
    tr.width(3)

    for _ in range(5):
        tr.forward(length)
        tr.right(144)


if __name__ == '__main__':
    star(150)


# ---------------------
def squared_in_squared(size):
    """Напишите программу, которая рисует квадраты, чтобы создать узор (квадрат в квадрате)"""
    tr.width(3)
    tr.speed(20)

    while size > 50:
        for _ in range(4):
            tr.left(90)
            tr.forward(size)

        size -= 12


if __name__ == '__main__':
    squared_in_squared(500)
    tr.done()


# ---------------------
def labyrinth(size):
    """Напишите программу, которая рисует узор(лабиринт)"""
    tr.speed(5)
    tr.width(3)

    while size > 5:
        tr.right(90)
        tr.forward(size)

        size -= 10


if __name__ == '__main__':
    labyrinth(150)

# ---------------------
import turtle as tr


def dotted_line():
    """Напишите программу, которая рисует пунктирную линию"""

    tr.Screen().setup(500, 500)
    tr.penup()
    tr.shape('circle')

    for _ in range(8):
        tr.dot(20)
        tr.forward(25)


if __name__ == "__main__":
    dotted_line()
    tr.done()

# ---------------------
import turtle as tr

tr.Screen().setup(500, 500)
tr.pensize(3)


def rectangle():
    """Напишите программу, которая рисует прямоугольник с точкой в каждом углу"""
    for x in ((200, 100) * 2):
        tr.dot(15)
        tr.forward(x)
        tr.right(90)


if __name__ == '__main__':
    rectangle()
    tr.done()

# ---------------------
import turtle as tr


def cobweb():
    """Напишите программу для рисования паутины в соответствии с примером. Программа должна считывать
    количество лучей паутины, число n."""

    tr.pensize(3)
    tr.shapesize(stretch_wid=2, stretch_len=None, outline=None)
    tr.dot(20)

    for _ in range(8):
        tr.forward(150)
        tr.stamp()
        tr.back(150)
        tr.left(45)


if __name__ == '__main__':
    cobweb()
    tr.done()

# ---------------------
import turtle as tr


def circle_tr():
    """Напишите программу, которая рисует круг из черепашек """
    tr.shape('turtle')
    tr.shapesize(2)
    tr.stamp()
    tr.penup()

    for _ in range(10):
        tr.forward(100)
        tr.stamp()
        tr.backward(100)
        tr.left(36)


if __name__ == '__main__':
    circle_tr()
    tr.done()

# ---------------------
import turtle as tr


def clock_face():
    """Напишите программу, которая рисует циферблат часов (в виде черепашек) на цветном фоне"""
    tr.Screen().colormode(255)
    tr.Screen().bgcolor(209, 235, 255)
    tr.Screen().setup(600, 600)

    tr.speed(5)

    tr.shape('turtle')
    tr.penup()
    tr.pensize(5)
    tr.shapesize(2)

    for _ in range(12):
        tr.forward(160)
        tr.pendown()
        tr.forward(20)
        tr.penup()
        tr.forward(20)
        tr.stamp()
        tr.backward(200)
        tr.left(30)


if __name__ == '__main__':
    clock_face()
    tr.done()

# ---------------------
import turtle as tr


def clock_face():
    """Напишите программу, которая рисует спираль (в виде черепашек) на цветном фоне"""
    tr.Screen().colormode(255)
    tr.Screen().bgcolor(129, 230, 129)
    tr.Screen().setup(600, 600)

    tr.speed(3)
    tr.shape('turtle')
    tr.penup()

    for i in range(50):
        tr.right(20)
        tr.forward(i)
        tr.stamp()


if __name__ == '__main__':
    clock_face()
    tr.done()

# ---------------------
import turtle as tr


def pattern():
    """Напишите программу, которая рисует узор (разноцветный, увеличивающейся спиралью)"""
    tr.Screen().setup(700, 700)
    tr.speed(3)

    color = ("green", "purple", "orange", "red", "blue", "yellow")
    ind = 4
    tr.ht()

    for i in range(1, 45):
        tr.pensize(i)
        tr.pencolor(color[ind])
        tr.left(45)
        tr.forward(i * 5)
        ind += 1
        if ind > 5:
            ind = 0


if __name__ == '__main__':
    pattern()
    tr.done()

# ---------------------
import turtle as tr


def david_star():
    """Напишите программу, которая рисует звезду Давида. Такую звезду можно создать из двух треугольников."""
    for _ in range(3):
        tr.forward(150)
        tr.right(120)

    tr.penup()

    tr.right(90)
    tr.forward(90)
    tr.left(90)

    tr.pendown()

    for _ in range(3):
        tr.forward(150)
        tr.left(120)


if __name__ == '__main__':
    david_star()
    tr.done()

# ---------------------
import turtle as tr


def rays():
    """Лучи"""

    tr.Screen().colormode(255)
    tr.ht()
    tr.speed(10)
    tr.pencolor(74, 201, 143)
    tr.pensize(2)

    for cord in range(-450, 451, 100):
        tr.pendown()
        tr.goto(cord, -450)
        tr.dot(7, "blue")
        tr.penup()
        tr.goto(0, 0)

    tr.dot(7, (250, 121, 0))


if __name__ == '__main__':
    rays()
    tr.done()

# ---------------------
import turtle as tr


def olympic_circle():
    """Напишите программу, которая рисует изображение символа олимпиады"""
    tr.speed(11)
    tr.Screen().setup(500, 500)
    tr.pensize(2)

    for coords, color in zip(((0, -50), (100, -50), (-100, -50), (-50, -120), (50, -120)),
                             ("Black", "Red", "Blue", "Yellow", "Green")):
        tr.penup()
        tr.goto(coords)
        tr.pendown()
        tr.pencolor(color)
        tr.circle(50)


if __name__ == '__main__':
    olympic_circle()
    tr.done()

# ---------------------
import turtle as tr


def bear():
    """Напишите программу, которая рисует изображение мишки"""
    tr.speed(11)
    tr.Screen().setup(1000, 1000)
    tr.pensize(2)
    # ----------------

    tr.circle(10)
    for i in ((0, -80), (0, -120)):
        tr.goto(i)
        tr.penup()

    tr.pendown()
    for i in (80, 150):
        tr.circle(i)

    tr.penup()
    for i in ((70, 35), (-70, 35)):
        tr.goto(i)
        tr.dot(28)

    for i in ((100, 153), (-100, 153)):
        tr.goto(i)
        tr.pendown()
        tr.circle(45)

        tr.penup()


if __name__ == '__main__':
    bear()
    tr.done()

# ---------------------
