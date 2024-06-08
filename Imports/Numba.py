# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Модуль numba ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import numba
from time import time


@numba.njit(cache=True)
def Eulers_hypothesis(num):
    for a in range(1, num):
        for b in range(1, num):
            for c in range(1, num):
                for d in range(1, num):
                    for e in range(1, num):
                        if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                            return f"a + b + c + d + e = {a + b + c + d + e}\n" \
                                   f"a = {a}\nb = {b}\nc = {c}\nd = {d}\ne = {e}"


if __name__ == '__main__':
    start_time = time()
    print(Eulers_hypothesis(150))
    end_time = time() - start_time

    print(f"Время выполнения: {end_time} секунд")
