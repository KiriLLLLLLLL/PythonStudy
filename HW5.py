__author__ = 'Ермаченков Кирилл'


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
import sys

def mk_dirs(new_dir):
    if os.path.exists(new_dir):
        print(f'Невозможно создать папку {new_dir}, она уже существует')
    else:
        os.mkdir(new_dir)
        print(f'Папка {new_dir} успешно создана!')

def rm_dirs(rm_dir):
    if os.path.exists(rm_dir):
        shutil.rmtree(rm_dir)
        print(f'Папка {rm_dir} успешно удалена!')
    else:
        print(f'Невозможно удалить папку {rm_dir}, ее не существует')



for i in range(1, 10):
    mk_dirs(f'dir_{i}')
    rm_dirs(f'dir_{i}')



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def ls_dirs(key='d'):
    for i in os.listdir():
        if key == 'd':
            if os.path.isdir(i):
                print(i)
        elif key == 'a':
                print(i)
        else:
            print(f'{key} - неизвестный ключ.')
            break



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def cp():
    file = os.path.basename((sys.argv[0]))
    cp_path = os.path.realpath((sys.argv[0]))
    shutil.copy(cp_path, f'copy_{file}')

cp()


























