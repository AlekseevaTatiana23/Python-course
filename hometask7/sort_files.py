'''
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

from pathlib import Path
import os
import shutil
from random import choices, randint
from string import ascii_lowercase, digits
import os

def sort_files(path:str | Path, groups:dict[str:list[str]]=None) -> None:
    if not groups:
        groups = {
            Path('video'): ['avi', 'mov', 'mk4'],
            Path('images'): ['bmp', 'jpeg', 'jpg', 'png']
        }
    os.chdir(path)
    reverse_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for ext in ext_list:
            reverse_groups[f'{ext}']= target_dir
    print(reverse_groups)
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


def gen_files(ext:str, min_name: int=6, max_name:int = 30, min_size:int=256,
              max_size:int = 4096, file_count:int = 42) ->None:
    for _ in range(file_count):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


def num_files(directory: str | Path, **kwargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for ext, num in kwargs.items():
        gen_files(ext, file_count=num)
