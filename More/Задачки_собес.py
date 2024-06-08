# Определить кол-во черных квадратов на шахматной доске:
# Проверить assert-ом правильность подсчета кол-ва


def size_chess_board(n: int, m: int):
    """ПОДСКАЗКА: Слева снизу (A1) черный квадрат"""
    number_of_squares = n * m
    if number_of_squares % 2 != 0:
        return (number_of_squares // 2) + 1
    else:
        return number_of_squares // 2


func: object = size_chess_board(11, 11)

assert size_chess_board(11, 11) == 60, f"Верное кол-во черных квадратов: {func}, {size_chess_board.__doc__}"

# {size_chess_board.__doc__}  # Вызов справки по функции

# ======================================================================

# inplace алгоритмы:
# Удаление повторяющихся элементов:

import sys


def remove_dublicates(nums: list) -> list:
    first_point, second_pointer = 0, 0

    while second_pointer < len(nums):
        while second_pointer < len(nums) - 1 and nums[second_pointer] == nums[second_pointer + 1]:
            second_pointer += 1

        nums[first_point] = nums[second_pointer]
        first_point += 1
        second_pointer += 1
    return nums[:first_point]


print(remove_dublicates([0, 0, 1, 1, 1, 2, 2, 3, 4]))
print(sys.getsizeof(remove_dublicates([0, 0, 1, 1, 1, 2, 2, 3, 4])))  # проверка используемой памяти


# Моё решение:

def set_unique(collection: list) -> list:
    collection.insert(0, [])

    for i in collection[1::]:
        if i not in collection[0]:
            collection[0].append(i)

    collection = collection[0]
    return collection


print(set_unique([0, 0, 1, 1, 1, 2, 2, 3, 4]))
print(sys.getsizeof(set_unique([0, 0, 1, 1, 1, 2, 2, 3, 4])))  # проверка используемой памяти

# ======================================================================

# Вызов случайной карты из колоды:

import random


class RandomCard:
    def __init__(self) -> None:
        self._rank = [
            '2-ку', '3-ку', '4-ку', '5-ку', '6-ку', '7-ку', '8-ку', '9-ку', '10-ку',
            'Валетa', 'Даму', 'Короля', 'Туза'
        ]
        self._suit = [
            'Червы', 'Бубны', 'Трефы', 'Пики'
        ]

    def generation_random_card(self) -> str:
        _rank = random.choice(self._rank)
        _suit = random.choice(self._suit)
        return f"Вы вытянули: {_rank} {_suit}"


card = RandomCard()
print(card.generation_random_card())

# ======================================================================
# Сколько преодолеет человек вершин и низин, если его путь бы составил DDUUD (D-Down, U-UP)

travel_map = input().upper()
ALPHABET = 'DU'  # разрешенные символы


def calculation(x: str) -> (str, int):
    sea_level = 0  # уровень моря
    peak = 0  # кол-во преодоленных вершин
    pit = 0  # кол-во преодоленных впадин

    for i in x:
        if i not in ALPHABET:
            raise TypeError("Неверно введено значение: Введите вершину(U, u) и\или впадину(D, d)")
        if i in 'U':
            sea_level += 1
            if sea_level > 0 and not sea_level > 1:
                peak += 1
        if i in 'D':
            sea_level -= 1
            if sea_level < 0 and not sea_level < -1:
                pit += 1
    return f"Вершины преодолены: {peak}\nНизины преодолены: {pit}"


if __name__ == "__main__":
    result = calculation(travel_map)
    print(result)

assert calculation("DDUUD") == f"Вершины преодолены: {0}\nНизины преодолены: {2}"

# ======================================================================
# Вернуть 2 значения из массива, которые при сумме будут равняться числу k:

k = 0

letter = [-2, -1, 1, 2]

for i in letter:
    for y in (reversed(letter)):
        if i + y == k:
            print([i, y])
        break

# ======================================================================
