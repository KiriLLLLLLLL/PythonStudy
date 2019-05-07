import os
import lib_mod as lm 

def change_dir (path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - папки не существует'.format(path))

def start ():
    answer =''
    while answer != '5':
        print('----------------------------------------')
        print('Текущая директория: ' + os.getcwd())
        answer = input('Выберите пункт меню:\n'
                       '1. Перейти в папку\n'
                       '2. Поcмотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n')
        if answer =='5':
            break
        if answer == '1':
            path_name = input('Укажите папку для перехода: ')
            print(change_dir(path_name))
        elif answer == '2':
            lm.list_dir()
        elif answer == '3':
            name = input('Введите имя удаляемой папки: ')
            lm.rem_fol(name)
        elif answer == '4':
            name = input('Введите имя новой папки: ')
            lm.chek_fol(name)


start()
