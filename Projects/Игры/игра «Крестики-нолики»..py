def welcome_func():
    return (f"---------------------\n"
            f"Игра крестики-нолики!\n"
            f"---------------------\n"
            f"Правила игры:\n"
            f"1. Участвуют 2 игрока. Первый делает ход 'x'.\n"
            f"2. Ввод координат в формате 'XX' через пробел.\n"
            f"3. Первая координата по диагонали, вторая по вертикали.\n"
            f"4. Используются только цифры от 0 до 2(включительно).\n"
            f"5. При некорректном вводе или уже занятой клетке, игрок делает ход вновь.\n"
            f"6. После каждого хода, обновленное игровое поле отображается.\n"
            f"--- Удачи ---\n")


# -----------------------


def playing_field(matrix_field):
    special_symbols = "012"
    print("  0 1 2")

    for index, value in enumerate(matrix_field):
        print(special_symbols[index], *value)


# -----------------------
def checking_correct_input(input_coords):
    correct_symbols = ['0', '1', '2']

    if len(input_coords) == 2:
        if input_coords[0] in correct_symbols and input_coords[1] in correct_symbols:
            return True
    return False


# -----------------------
def win_combinations():
    win_coords = [
        [[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], [[0, 2], [1, 1], [2, 0]],
        [[1, 0], [1, 1], [1, 2]], [[0, 2], [1, 2], [2, 2]], [[2, 0], [2, 1], [2, 2]]
    ]
    return win_coords


# -----------------------
def check_combination(coords_player):
    winner_combination = 0

    for all_comb in win_combinations():

        for coord in all_comb:
            if coord in coords_player:
                winner_combination += 1

        if winner_combination == 3:
            break
        else:
            winner_combination = 0

    return winner_combination


# -----------------------
def player_x_func():
    while True:
        playing_field(board_matrix)

        player_x = input("\n----------------------\nИгрок (x) вводит координаты: ").split()

        if checking_correct_input(player_x):
            v0 = int(player_x[0])
            v1 = int(player_x[1])

            if [v0, v1] not in un_coords_array:
                board_matrix[v0][v1] = 'x'

                for array in [array_coords_player_x, un_coords_array]:
                    array.append([v0, v1])

                break

            else:
                print("***Клетка занята! Введите другие координаты***\n")
                continue
        else:
            print("***Неверный формат. Попробуйте еще раз***\n")
            continue


# -----------------------
def player_o_func():
    while True:
        playing_field(board_matrix)

        player_o = input("\n----------------------\nИгрок (o) вводит координаты: ").split()

        if checking_correct_input(player_o):
            v0 = int(player_o[0])
            v1 = int(player_o[1])

            if [v0, v1] not in un_coords_array:
                board_matrix[v0][v1] = 'o'

                for array in [array_coords_player_o, un_coords_array]:
                    array.append([v0, v1])

                break

            else:
                print("***Клетка занята! Введите другие координаты***\n")
                continue
        else:
            print("***Неверный формат. Попробуйте еще раз***\n")
            continue


# -----------------------
print(welcome_func())

array_coords_player_x = []
array_coords_player_o = []
un_coords_array = []

board_matrix = [['-' for _ in range(3)] for _ in range(3)]

# -----------------------
while True:

    player_x_func()

    if check_combination(array_coords_player_x) > 2:
        playing_field(board_matrix)
        print("\n*****\n"
              "Крестик победил!\n"
              "*****")
        break

    if len(un_coords_array) == 9:
        playing_field(board_matrix)
        print("\n***Ничья***")
        break

    # -----
    player_o_func()

    if check_combination(array_coords_player_o) > 2:
        playing_field(board_matrix)
        print("\n*****\n"
              "Нолик победил!\n"
              "*****")
        break

    if len(un_coords_array) == 9:
        playing_field(board_matrix)
        print("\n***Ничья***")
        break
