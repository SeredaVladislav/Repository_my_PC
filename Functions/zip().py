L = [i for i in range(10)]

M = [i for i in range(10, 0, -1)]

for a in zip(L, M):  # объединение списков
    print(a)

for a, b in zip(L, M):  # перемножение 2-х списков
    print('a =', a, 'b =', b, 'a*b =', a * b)

N = [a * b for a, b in zip(L, M)]  # перемножение 2-х списков
print(N)

text = 'aaabbccccdaa'

last = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == last:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += last + str(count)  # иначе - записываем в результат
        last = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += last + str(count)  # и добавляем в результат последний символ
print(result)