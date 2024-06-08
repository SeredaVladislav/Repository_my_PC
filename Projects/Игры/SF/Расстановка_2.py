import random

# ---------------------------
reserved_cells = set()  # Клетки рядом с кораблями


def func_lock(input_coords, x, y):
    for i in input_coords:
        if i not in reserved_cells:
            # Крайние координаты (по горизонтали (x)) от выстрела (для запрета)
            x1 = str(x) + str(y - 1)
            x2 = str(x) + str(y + 1)
            # ---------------------------
            # Крайние координаты (по вертикали (y)) от выстрела (для запрета)
            # y1 = str(x - 1) + str(y)
            # y2 = str(x + 1) + str(y)
            # ---------------------------

            all_res_cells = [x1, x2]

            for c in all_res_cells:
                reserved_cells.add(c)

            reserved_cells.add(i)

            return True


# --------------------------
coords_of_single_ship = []  # Координаты кораблей

ship1 = 0
while ship1 < 4:
    x_single_ship = random.randint(1, 6)
    y_single_ship = random.randint(1, 6)

    random_coordinates = [str(x_single_ship) + str(y_single_ship)]

    if func_lock(random_coordinates, x_single_ship, y_single_ship):
        ship1 += 1
        coords_of_single_ship.append(*random_coordinates)

    else:
        continue

# --------------------------
ship2 = 0
while ship2 < 2:
    x_single_ship = random.randint(1, 6)
    y_single_ship = random.randint(1, 6)

    random_coordinates = [str(x_single_ship) + str(y_single_ship)]

    if func_lock(random_coordinates, x_single_ship, y_single_ship):
        ship2 += 1
        coords_of_single_ship.append(*random_coordinates)

    else:
        continue

# --------------------------

def hits(x, y, fld):
    """ Добавление кораблей по индексам(координатам) в матрицу """
    fld[x][y] = "■ |"


# ---------------------------
# ---------------------------
# ---------------------------
def output_board(ai_field_arg):
    """ Вывод итогового поля с расстановкой кораблей в консоль """
    print('  | 1 | 2 | 3 | 4 | 5 | 6 |')
    for l_side, crds in enumerate(ai_field_arg):
        print(l_side + 1, "|", *crds)


ai_field = [['o |' for _ in range(6)] for _ in range(6)]  # Координатная матрица поля

for i in coords_of_single_ship:  # Цикл для функции hits(). Формирование аргументов с координатами.
    hits(int(i[0]) - 1, int(i[1]) - 1, ai_field)

output_board(ai_field)
# ---------------------------
# ---------------------------
# ---------------------------

