a, b = int(input()), int(input())

time_sum_div = 0

num_max_div = 0
sum_div = 0

for num in range(a, b + 2):
    if time_sum_div >= sum_div:
        sum_div = time_sum_div
        num_max_div = num - 1
    time_sum_div = 0
    if num > b:
        break
    for div in range(1, num + 1):
        if num % div == 0:
            time_sum_div += div

print(num_max_div, sum_div)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = int(input())

for num in range(1, n + 1):
    plus = 0
    for div in range(1, num + 1):
        if num % div == 0:
            plus += 1
    print(n, "{n_string}{'+' * plus}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = int(input())

temp_var = 0

while True:
    temp_var += n % 10
    n //= 10
    if n < 1:
        n = temp_var
        temp_var = 0
        if n < 10:
            print(n)
            break
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from math import factorial

n = int(input())

sum_fact = 0

for num in range(1, n + 1):
    sum_fact += factorial(num)

print(sum_fact)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a, b = int(input()), int(input())

for num in range(a, b + 1):
    temp_var = 0

    for div in range(1, num + 1):
        if num % div == 0:
            temp_var += 1

    if temp_var == 2:
        print(num)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = 8
count = 0
maximum = -10 ** 12

for i in range(n):
    x = int(input())

    if abs(x) > 10 ** 12:
        continue
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = 8
count = 0
maximum = -10 ** 12  # Установим начальное максимальное значение как минимально возможное

for i in range(n):
    x = int(input())
    if abs(x) <= 10 ** 12:  # Проверяем, чтобы введенное число не превышало абсолютное значение 10 в 12 степени
        if x % 4 == 0:
            count += 1
            if x > maximum:
                maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n = 8
count = 0
maximum = -10 ** 12
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x < maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = 4
count = 0
maximum = -10 ** 8
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = int(input())

print('*' * 19)
for i in range(1, n - 1):
    print('*' + ' ' * 17 + '*')
print('*' * 19)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = int(input()[2])
print(n)

num = int(input())

count_3 = 0
last_digit = num % 10
count_last_digit = 0
count_even = 0
sum_greater_than_5 = 0
product_greater_than_7 = 1
count_0_5 = 0

while num > 0:
    digit = num % 10
    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last_digit += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_greater_than_5 += digit
    if digit > 7:
        product_greater_than_7 *= digit
    if digit == 0 or digit == 5:
        count_0_5 += 1
    num //= 10
if product_greater_than_7 == 1 and num > 7:
    product_greater_than_7 = num

print(count_3)
print(count_last_digit)
print(count_even)
print(sum_greater_than_5)
print(product_greater_than_7)
print(count_0_5)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
interesting_numbers = []
count = 0

for i in range(10, 1000):
    for j in range(i, 1000):
        if (i ** 3 + j ** 3) ** (1 / 3) % 1 == 0 and i != j:
            interesting_numbers.append(i ** 3 + j ** 3)
            count += 1

            if count == 5:
                break

    if count == 5:
        break

interesting_numbers.sort()
print(interesting_numbers)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
text_string = input()

overlap = 0
letter = ""

for symbol in text_string:
    if text_string.count(symbol) >= overlap:
        overlap = text_string.count(symbol)
        letter = symbol

print(letter)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
text_string = input()

if text_string.count("sharp") < 1:
    print("NO")
elif text_string.count("sharp") > 1:
    print((text_string.find("sharp")), len(text_string) - (text_string[::-1]).find("sharp") - 1)
else:
    print(text_string.find("sharp"))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
text_string = input()

print(text_string[:text_string.find("obj_func_map")] + text_string[text_string.rfind("obj_func_map") + 1:])

s = 'In {0}, someone paid {1} {2} for two pizzas.'

print(s.format("2010", "10k", "Bitcoin"))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n = int(input())
n_string = [int(input()) for _ in range(n)]

sum_numbers = []

while len(n_string) > 1:
    sum_numbers.append(n_string[0] + n_string[1])
    del n_string[0]

print(sum_numbers)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = 5
n_string = [1, 2, 3, 4, 5]
l = []

for i in range(len(n_string) + 1):
    if len(l) == n - 1:
        break
    l.append(n_string[i] + n_string[i + 1])

n_string.clear()
n_string.extend(l)
l.clear()

print(n_string)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n = int(input())
n_string = [int(input()) for _ in range(n)]

print(n_string[::2])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = int(input())
n_string = [input() for _ in range(n)]
k = int(input())

for i in n_string:
    if len(i) < k:
        pass
    else:
        print(i[k - 1], end="")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n = int(input())
n_string = [input() for _ in range(n)]

list_word = []

for i in n_string:
    list_word.extend(i)

print(list_word)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n = int(input())
n_string = [input() for _ in range(n)]

k = int(input())
k_string = [input().lower() for _ in range(k)]

for i in n_string:
    low_string = i.lower()
    if all(j in low_string for j in k_string):
        print(i)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n_str = [input() for _ in range(int(input()))]
k_str = [input().lower() for _ in range(int(input()))]

for i in n_str:
    if all(j in i.lower() for j in k_str):
        print(i)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n_number = [int(input()) for _ in range(int(input()))]

list_pos, list_zero, list_neg = [], [], []

for i in n_number:
    if i < 0:
        list_pos.append(i)
    elif i == 0:
        list_zero.append(i)
    else:
        list_neg.append(i)

print(*(list_pos + list_zero + list_neg), sep='\n')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n = [int(input()) for _ in range(int(input()))]

product_num = int(input())

need_num = 0
flag = 0

while True:
    if flag == len(n):
        print("НЕТ")
        break
    if need_num > 0:
        print('ДА')
        break
    for i in range(1, len(n)):
        if flag == i:
            continue
        if n[flag] * n[i] == product_num:
            need_num += 1

    flag += 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

options = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class SublistList:
    def sublist(self, symbols: list) -> list[list]:

        result = []

        result.append([])
        start = 0
        finish = 0
        flag_finish = 0

        while True:
            finish += 1
            result.append(symbols[start:finish])
            start += 1

            if result[-1] == symbols:
                break

            if finish == len(symbols):
                flag_finish += 1
                finish = flag_finish
                start = 0

        return result


if __name__ == "__main__":
    obj_func = SublistList()
    print(obj_func.sublist(input().split()))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        d = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        }

        for i in range(len(s) - 1):
            if d[s[i]] >= d[s[i + 1]]:
                result += d[s[i]]
            else:
                result -= d[s[i]]
        result += d[s[-1]]

        return result


if __name__ == "__main__":
    obj_solution = Solution()
    func_romanToInt = obj_solution.romanToInt("LVIII")
    # assert func_palindrome == 1994
    print(func_romanToInt)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        res = ""
        n = 0

        while min(map(len, strs)) > len(res):

            for i in strs:
                result += i[n]

            if result.count(result[0]) == len(result):
                n += 1
                res += result[0]
                result = ""

            else:
                break
        return res


if __name__ == "__main__":
    obj_solution = Solution()
    func_longestCommonPrefix = obj_solution.longestCommonPrefix([""])
    # assert func_palindrome == 1994
    print(func_longestCommonPrefix)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Solution:
    def __init__(self, list_numbers: list) -> None:
        self.list1 = list_numbers

        self.res = []
        for i in list_numbers:
            self.res += i

    def bubble_sort(self) -> list:
        flag = self.res
        n = len(flag)

        for i in range(n - 1):
            finish = None
            for j in range(n - i - 1):
                if flag[j] > flag[j + 1]:
                    finish = True
                    flag[j], flag[j + 1] = flag[j + 1], flag[j]

            if finish is None:
                break

        return flag


if __name__ == "__main__":
    quantity_inp = int(input())
    numbers = [list(map(int, input().split())) for _ in range(quantity_inp)]

    obj_Solution = Solution(numbers)
    func_bubble_sort = obj_Solution.bubble_sort()
    print(*func_bubble_sort)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Корректность пароля:

class Solution:
    def __init__(self, password) -> None:
        self.password = password
        self._ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        self._ALPHABET_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._NUMBER = "0123456789"

    def is_password_good(self) -> bool:
        user_password = self.password
        access = False
        _password_cells = [0, 0, 0]

        if len(user_password) >= 8:
            for i in user_password:
                if i in self._ALPHABET:
                    _password_cells[0] += 1
                elif i in self._ALPHABET_UP:
                    _password_cells[1] += 1
                elif i in self._NUMBER:
                    _password_cells[2] += 1

        if 0 not in _password_cells:
            access = True

        return access


if __name__ == "__main__":
    password_input = input()
    obj_Solution = Solution(password_input)
    func_is_password_good = obj_Solution.is_password_good()
    print(func_is_password_good)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class NumberToWordsClass:
    def __init__(self) -> None:
        self._numbers = {
            '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять',
            '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '10': 'десять',
            '11': 'одиннадцать', '12': 'двенадцать', '13': 'тринадцать', '14': 'четырнадцать',
            '15': 'пятнадцать', '16': 'шестнадцать', '17': 'семнадцать', '18': 'восемнадцать',
            '19': 'девятнадцать',
        }
        self._numbers_more_10 = "надцать"
        self._number_20_30 = "дцать"
        self._number_40 = "сорок"
        self._number_50_60_70_80 = "десят"
        self._numbers_more_90 = "девяносто"

    def number_to_words(self, num):
        if 0 < num < 20:
            print(self._numbers[str(num)])
        elif num in [20, 30]:
            print(self._numbers[str(num // 10)] + self._number_20_30)
        elif 20 < num < 40:
            print(self._numbers[str(num // 10)] + self._number_20_30, self._numbers[str(num)[1]])
        elif num == 40:
            print(self._number_40)
        elif 40 < num < 50:
            print(self._number_40, self._numbers[str(num)[1]])
        elif num in [50, 60, 70, 80]:
            print(self._numbers[str(num // 10)] + self._number_50_60_70_80)
        elif 50 < num < 90:
            print(self._numbers[str(num // 10)] + self._number_50_60_70_80, self._numbers[str(num)[1]])
        elif num == 90:
            print(self._numbers_more_90)
        else:
            print(self._numbers_more_90, self._numbers[str(num)[1]])


if __name__ == '__main__':
    num_val = int(input())
    obj_class = NumberToWordsClass()
    obj_is_pangram = obj_class.number_to_words(num_val)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MonthClass:
    def __init__(self) -> None:
        self.month = {
            1: ["january", "январь"], 2: ["february", "февраль"], 3: ["march", "март"], 4: ["april", "апрель"],
            5: ["may", "май"], 6: ["june", "июнь"], 7: ["july", "июль"], 8: ["august", "август"],
            9: ["september", "сентябрь"], 10: ["october", "октябрь"], 11: ["november", "ноябрь"],
            12: ["december", "декабрь"]
        }

    def get_month(self, language_number):
        if language_number[0] == 'ru':
            print(self.month[int(language_number[1])][1])
        else:
            print(self.month[int(language_number[1])][0])


if __name__ == '__main__':
    language_number_val = [input() for _ in range(2)]
    obj_class = MonthClass()
    obj_get_month = obj_class.get_month(language_number_val)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class IsMagicClass:
    def __init__(self) -> None:
        pass

    def is_magic(self, date) -> bool:
        num = date.split(".")
        return int(num[0]) * int(num[1]) == int(num[2][2:])


if __name__ == '__main__':
    date_val = input()
    obj_class = IsMagicClass()
    obj_get_month = obj_class.is_magic(date_val)
    print(obj_get_month)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class IsPangramClass:
    def __init__(self) -> None:
        self._ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def is_pangram(self, text) -> bool:
        flag = True

        for i in self._ALPHABET:
            if i not in text.upper():
                flag = False
                break

        return flag


if __name__ == '__main__':
    text_val = input()
    obj_class = IsPangramClass()
    obj_is_pangram = obj_class.is_pangram(text_val)
    print(obj_is_pangram)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


