expression = "2 + 3 * 5"

print(expression)  # 2 + 3 * 5

print(eval(expression))  # 17
# Выполняет код строки как выражение и возвращает результат, как если бы он был написан в программе

x = 5
y = 10
expression = "row + y"
result = eval(expression)
print(result)
# Вывод: 15

expression = "len('hello')"
result = eval(expression)
print(result)
# Вывод: 5

condition = True
expression = "10 if condition else 20"
result = eval(expression)
print(result)
# Вывод: 10

expression = "[1, 2, 3, 4, 5]"
result = eval(expression)
print(result)
# Вывод: [1, 2, 3, 4, 5]


# шифр Цезаря: (Дешифровка)
eval(
    "(a := 'abcdefghijklmnopqrstuvwxyz'), (number_pairs :=int(input())), (print(*[a[a.find(symbol) - number_pairs] for symbol in input()], sep=''))")
