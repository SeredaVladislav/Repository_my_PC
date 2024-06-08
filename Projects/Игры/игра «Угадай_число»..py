from random import randint


class GuessTheNumber:
    """Угадывание числа в диапазоне"""

    def __init__(self, start, finish) -> None:
        """Конструктор"""
        self.random_number = None
        self.start = start
        self.finish = finish

    def numbers_gen(self) -> None:
        """Функция генератора случайного числа"""
        self.random_number = randint(self.start, self.finish)

    def guess_number(self, value):
        attempt_user = 0

        while True:
            if attempt_user == attempt_user_input:
                print("Проигрыш!\n"
                      "Вы использовали все попытки\n")
                break

            try:
                user_input = int(input(f"Введите число в диапазоне от {self.start} до {self.finish}: "))
            except error:
                print("Значение не является числом!\n"
                      "Попробуйте еще раз.\n")

            else:
                attempt_user += 1
                if user_input > self.finish or user_input < self.start:
                    print(f"\nВы вышли за границы диапазона!\n"
                          f"Ваш диапазон от {self.start} до {self.finish}\n")

                elif user_input > self.random_number:
                    print(f"Слишком много, попробуйте ввести число меньше {user_input}\n")
                elif user_input < self.random_number:
                    print(f"Слишком мало, попробуйте ввести число больше {user_input}\n")
                elif user_input == self.random_number:
                    print("\nВы угадали, поздравляем!\n"
                          f"Количество попыток использовано: {attempt_user}/{attempt_user_input}")
                    break


while True:
    try:
        start_number = int(input("Введите первое число диапазона: "))
        finish_number = int(input("Введите второе число диапазона: "))
        attempt_user_input = int(input("Введите количество попыток для победы в игре: "))
    except ValueError as error:
        print("Значение не является числом!\n"
              "Попробуйте еще раз.\n")
    else:
        if finish_number - start_number <= attempt_user_input:
            print("\nКоличество попыток превышает допустимое!\n"
                  "Начните заново.")
            continue

        game_guess_number = GuessTheNumber(start_number, finish_number)
        game_guess_number.guess_number(game_guess_number.numbers_gen())
        break

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
