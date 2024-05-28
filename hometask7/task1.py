# Напишите функцию группового переименования файлов.
# Она должна:
# a. принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from pathlib import Path

def rename_group_files(new_name: str, id_len: int, ext: str, new_ext: str, range_name:list[int], path: Path):
    work_path = Path.cwd() if path is None else Path(path)
    file_id = 1
    for file in work_path.iterdir():
        if file.is_file() and file.suffix == ext:
            os.rename(file, (f"{file.split('.')[0][range_name[0]:range_name[1]]}"
                                           f"{new_name}{file_id:0>{id_len}}.{new_ext}"))  #переименование файла по условию
            file_id += 1


if __name__ == '__main__':
    rename_group_files('new', 4, 'png', 'zip', [2, 4], "C:/Users/user/PycharmProjects/Python-course")