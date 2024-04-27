# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

counter = 0
attempt_amount = 10
from random import randint

num = randint(LOWER_LIMIT, UPPER_LIMIT)

while counter <= attempt_amount:
    user_num = int(input(f'Угадайте загаданное число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if user_num != num:
        print('Введенное число больше загаданного' if user_num > num else 'Введенное число меньше загаданного')
        counter += 1
    else:
        print('Поздравляю! Вы угадали число!')
        break
print("Попытки закончились")