"""
Задача 2 Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

"""

from random import randint
from sys import argv
def guess_number(low:int, up:int, counter:int) -> bool:
    guess = randint(low, up)
    for _ in range(counter):
        number = int(input('Введите число: '))
        if number < guess:
            print('Загаданное число больше!')
        elif number > guess:
            print('Загаданное число меньше!')
        else:
            print('Вы угадали число!')
            return True
    print('Вы не угадали число! Попытки закончились!')
    return False


if __name__ == '__main__': # используется как отладчик для того чтобы не запускалось в других файлах
    param = argv[1:]
    guess_number(*(int(item) for item in param ))
