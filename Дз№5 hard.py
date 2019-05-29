__author__ = 'Ермаченков Кирилл'





import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - копия файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - сменить дирректорию на указанную")
    print("ls - отображение полного пути текущей дирректории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def rem_dir():
    if not file_name:
        print("Необходимо указать имя файла вторым аргументом")
        return
    if input(f'Удалить {file_name}? Да(Y)/Нет(N) ').lower() not in (('д', 'да', 'y', 'yes')):
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        os.remove(file_path)
        print('Файл {} успешно удален'.format(file_name))
    except FileNotFoundError:
        print('Невозможно удалить {} - такой файл не существует'.format(file_name))

def ch_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(path)
        print('Вы успешно перешли в дирректорию {}'.format(dir_name))
        print(os.getcwd())
    except FileNotFoundError:
        print('Невозможно перейти в {} - такой дирректории не существует'.format(dir_name))

def ping():
    print("pong")

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым аргументом")
        return
    file_name_copy = str("copy_" + file_name)
    file_path = os.path.join(os.getcwd(), file_name_copy)
    try:
        copyfile(file_name, file_path)
        print('Файл {} создан'.format(file_name_copy))
    except FileExistsError:
        print('Файл {} уже существует'.format(file_name))
    except FileNotFoundError:
        print('Файл {} не существует'.format(file_name))

def full_path():
    path = os.getcwd()
    print(path)

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "rmdir": rem_dir,
    "cp": copy_file,
    "ls": full_path,
    "cd": ch_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[3]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
