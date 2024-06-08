# 1. Интерфейс приложения должен представлять собой консольное окно с двумя полями 6х6 вида:
#   | 1 | 2 | 3 | 4 | 5 | 6 |
# 1 | О | О | О | О | О | О |
# 2 | О | О | О | О | О | О |
# 3 | О | О | О | О | О | О |
# 4 | О | О | О | О | О | О |
# 5 | О | О | О | О | О | О |
# 6 | О | О | О | О | О | О |
# ------------------
# 2. Игрок играет с компьютером. Компьютер делает ходы наугад, но не ходит по тем клеткам, в которые он уже ходил.
# ------------------
# 3. Для представления корабля опишите класс Ship с конструктором, принимающим в себя набор точек (координат) на
# игровой доске.
# ------------------
# 4. Опишите класс доски. Доска должна принимать в конструкторе набор кораблей.
# ------------------
# 5. Корабли должны находится на расстоянии минимум одной клетки друг от друга.
# ------------------
# 6. Корабли на доске должны отображаться следующим образом:
#   | 1 | 2 | 3 | 4 | 5 | 6 |
# 1 | ■ | ■ | ■ | О | О | О |
# 2 | О | О | О | ■ | ■ | О |
# 3 | О | О | О | О | О | О |
# 4 | ■ | О | ■ | О | ■ | О |
# 5 | О | О | О | О | ■ | О |
# 6 | ■ | О | ■ | О | О | О |
# ------------------
# 7. На каждой доске (у ИИ и у игрока) должно находится следующее количество кораблей:
# 1 корабль на 3 клетки;
# 2 корабля на 2 клетки;
# 4 корабля на одну клетку.
# ------------------
# 8. Запретите игроку стрелять в одну и ту же клетку несколько раз. При ошибках хода игрока должно возникать исключение.
# ------------------
# 9. Если возникают непредвиденные ситуации, выбрасывать и обрабатывать исключения.
# ------------------
# 10. Буквой X помечаются подбитые корабли. Буквой T — промахи.
# ------------------
# 11. Побеждает тот, кто быстрее всех разгромит корабли противника.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from random import randint
from copy import deepcopy as dp


def hits(x, y, fld):
    fld[x][y] = "T |"

    return fld


def output_board(fld):
    print('  | 1 | 2 | 3 | 4 | 5 | 6 |')
    for lft_side, crds in enumerate(fld):
        print(lft_side + 1, "|", *crds)


def ai(all_sht):
    while True:
        ai_input_first_coord = str(randint(1, 6))
        ai_input_two_coord = str(randint(1, 6))

        if [ai_input_first_coord + ai_input_two_coord] not in all_sht:
            all_sht.append([int(ai_input_first_coord + ai_input_two_coord)])
            return int(ai_input_first_coord) - 1, int(ai_input_two_coord) - 1
        else:
            continue


# ------------------
def checking_correctness(plr_inpt_crds, all_sht):
    try:
        int(plr_inpt_crds)
    except ValueError:
        print("Введите только числа")

    else:

        try:
            if len(plr_inpt_crds) != 2:
                raise ValueError
        except ValueError:
            print("Введите только 2 координаты")

        else:

            try:
                if int(plr_inpt_crds[0]) not in range(1, 7) or int(plr_inpt_crds[1]) not in range(1, 7):
                    raise AttributeError
            except AttributeError:
                print("Выход на границы поля")

            else:

                try:
                    if [int(plr_inpt_crds)] in all_sht:
                        raise AttributeError
                except AttributeError:
                    print("В эту клетку уже стреляли")

                else:
                    return True


# ------------------
all_shots = []
ai_field = [['o |' for _ in range(6)] for _ in range(6)]
player_field = dp(ai_field)

while True:
    player_input_coords = input("Введите координаты: ")
    print()

    if checking_correctness(player_input_coords, all_shots):
        all_shots.append([int(player_input_coords)])
        hits(int(player_input_coords[0]) - 1, int(player_input_coords[1]) - 1, ai_field)
        print("Field AI\n---------------------------")
        output_board(ai_field)
        print("---------------------------\n")

    else:
        print("Попробуйте еще раз!")
        continue

    hits(*ai(all_shots), player_field)
    print("Field Player\n---------------------------")
    output_board(player_field)
    print("---------------------------\n")







#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
##
#
#
#
#
#

# ------------------
# class Ship:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def coords_shot(self):
#         return self.x, self.y
#
#
# ships = Ship(5, 2)
# playing_field(*ships.coords_shot())
# ------------------

# Определить рандомно корабли, расстояние 1 клетка между ними.
# board[x][y] = "X |"
# board[x][y] = "■ |"
# board[x][y] = "T |"

# ------------------
# Одно поле для 2-х игроков (возможно с помощью наследования классов), постоянно обновляемое с учетом списка(ходов) с
# координатами игрока, и расстановкой кораблей.
