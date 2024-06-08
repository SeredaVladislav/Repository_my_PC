squared_num = [2 << i for i in range(10)]  # [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print(squared_num)


# 2 << i == 2 ** i


# ------------------------------
def oppe(x: int, y: int) -> bool:
    """ Определение является ли, одно из целых чисел отрицательным, методом побитового сдвига. """
    return x ^ y < 0


if __name__ == '__main__':
    number_1 = 10
    number_2 = -15
    print(oppe(number_1, number_2))
