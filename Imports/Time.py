# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Модуль time ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time

seconds = time.time()
print("Секунды с начала эпохи =", seconds)  # время с 01.01.1970

print()

local_time = time.ctime(seconds)  # вывод текущего местного времени, за счет передачи времени с начала эпохи
print("Местное время:", local_time)

print()

start = time.time()  # Замер разницы времени при выполнении программы: Старт
print("Сейчас... ожидание")
time.sleep(2.4)  # ожидание перед выполнением программы
print("Через 2.4 секунды.")
print(time.time() - start)  # Время Старта - Текущее время после выполнения программы: 2.400017261505127

print()

result = time.localtime(seconds)
print(f"Только время: {result.tm_hour}:{result.tm_min}")
print("Только минуты:", result.tm_min)  # Минуты
print(f"Только дата: {result.tm_mday}-{result.tm_mon}-{result.tm_year}")
print("Только месяц: ", result.tm_mon)

print()
print("результат:", result)  # результат текущего времени с разбивкой

print("Год:", result.tm_year)  # Год
print("Часов:", result.tm_hour)  # Часы
print("Секунд:", result.tm_sec)  # Секунды
print("Дата:", result.tm_mday)  # Дата
