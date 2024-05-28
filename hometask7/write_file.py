'''
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''


from random import randint, uniform
from pathlib import Path

MIN_NUM = -1000
MAX_NUM = 1000

def write_file(num_str: int, name_file: str | Path) -> None:
    with open(name_file, 'w', encoding='utf-8') as f:
        for _ in range(num_str):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')