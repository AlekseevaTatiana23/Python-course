'''
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''

from random import randint, choice
from string import ascii_letters
from pathlib import Path

MIN_VALUE = 4
MAX_VALUE = 7

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def gen_names(num_str: int, name_file: str | Path) -> None:
    with open(name_file, 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            name = ''
            flag = choice([-1, 1])
            for _ in range(randint(MIN_VALUE, MAX_VALUE)):
                if flag == -1:
                    name += choice(consonants)
                else:
                    name += choice(vowels)
                flag *= -1
            f.write(name.title() + '\n')