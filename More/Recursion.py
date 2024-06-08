# -------------------------------------------- Рекурсия ----------------------------------------------------------------


def a(bb):
    bb += 1
    if bb == 100:
        return bb
    else:
        return a(bb)


print(a(1))


def recursion(x):  # функция
    if x < 5:  # условие, если...
        print(x)  # вывод значения х
        recursion(x + 1)  # вызов функции со значением х+1
        print(x)  # обратный вызов рекурсии при невыполнении условия с вызовом предыдущего значения


recursion(1)  # вызов функции с указанным значением


def factorial(x):  # функция
    if x == 1:  # условие, если...
        return 1  # возврат 1 если условие не выполнено
    return factorial(x - 1) * x  # возврат каждого предыдущего значения с (-1) с умножением на предыдущее


print(factorial(4))

number_user = int(input("Число: "))


def check(number_user: int):
    if number_user < 2:
        return not number_user % 2
    return check(number_user - 2)


if check(number_user):
    print("Четное")
else:
    print("Нечетное")

lists = [2, 7, 6, 8, 22, 13, 4]


def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])


print(min_list(lists))

num = 123456


def mirror(a, res=0):
    return mirror(a // 10, res * 10 + a % 10) if a else res


print(mirror(num))


def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)


print(equal(22, 4))


def f(n):
    print(n)
    if n < 3:
        f(n + 1)
    print('end {digit}')


f(1)


def rec(n):
    if len(n) == 1:
        return n[0]

    result = rec(n[1:])
    if result < n[0]:
        return result
    else:
        return n[0]


print(rec([5, 2, 9, 11]))

