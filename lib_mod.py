__author__ = 'Ермаченков Кирилл'


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

def chek_fol(path):
    if not os.path.exists(path):
        os.mkdir(path)
def rem_fol(path):
    if os.path.exists(path):
        shutil.rmtree(path)

pro_name = 'Дз№5'
path = os.getcwd()
print(path)

sel_act = int(input('Выберите действие: \n1 - создать папки; \n2 - удалить папки \nВведите число: '))

fullPath = os.path.join(path, pro_name)
chek_fol(fullPath)

if sel_act == 1:  
    for d in range(1, 10):
        lowPath = f"dir_{d}"
        direction = os.path.join(fullPath, lowPath)
        chek_fol(direction)
    print('Папки созданы!!!')

elif sel_act == 2:
    rem_fol(fullPath)

else:
    print('Вы ввели что-то не то! \nВнимательнее!!!')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


lstDir = os.listdir(path=fullPath)
print(lstDir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


os.system('copy Дз№5 easy.py newДЗ№5 easy.py')
print()

























