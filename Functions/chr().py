# Символам A..Z английского языка соответствуют номера с 65 по 90 в таблице символов ASCII.
# Символам a..z английского языка соответствуют номера с 97 по 122 в таблице символов ASCII.

alphabet = [chr(letter) for letter in range(65, 91)]
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
# 'V', 'W', 'X', 'Y', 'Z']

alphabet_2 = [chr(letter) for letter in range(97, 123)]
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
# 'v', 'w', 'x', 'y', 'z']


# Генератор пароля из латинских букв:
import random

length = int(input())  # длина пароля

alphabet_up = [chr(letter) for letter in range(65, 91)]
alphabet_low = [chr(letter) for letter in range(97, 123)]
alphabet_up.extend(alphabet_low)

end_index = len(alphabet_up) - 1

print(*[alphabet_up[random.randint(0, end_index)] for _ in range(length)], sep="")
