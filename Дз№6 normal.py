__author__ = 'Ермаченков Кирилл'

import lib_normal as n_lib

kids = [n_lib.Schoolkid('Иванов', 'А.В.', ['Иванова И.М.', 'Иванов С.П.'], '1А', ['Математика', 'Чтение', 'Физкультура']),
        n_lib.Schoolkid('Петров', 'Ф.В.', ['Петрова И.М.', ''], '1А', ['Математика', 'Чтение', 'Физкультура']),
        n_lib.Schoolkid('Сидоров', 'Л.Н.', ['Сидорова Д.К.', 'Сидоров С.У.'], '1А', ['Математика', 'Чтение', 'Физкультура']),
        n_lib.Schoolkid('Черепанова', 'В.В.', ['Стенькина И.М.', 'Черепанов С.С.'], '3А', ['Математика', 'Чтение', 'Физкультура', 'История']),
        n_lib.Schoolkid('Атясова', 'М.Ф.', ['Атясова И.М.', 'Атясов Ф.П.'], '3А', ['Математика', 'Чтение', 'Физкультура', 'История']),
        n_lib.Schoolkid('Жданов', 'Н.Г.', ['', 'Жданов В.П.'], '3А', ['Математика', 'Чтение', 'Физкультура', 'История']),
        n_lib.Schoolkid('Случин', 'П.П.', ['Случина Т.М.', 'Случин С.П.'], '5А', ['Математика', 'Чтение', 'Физкультура', 'История', 'Ин.язык']),
        n_lib.Schoolkid('Вдовин', 'А.В.', ['Вдовина И.М.', 'Вдовинов С.П.'], '5А', ['Математика', 'Чтение', 'Физкультура', 'История', 'Ин.язык']),
        n_lib.Schoolkid('Киренский', 'А.В.', ['Киренская И.М.', 'Киренский С.П.'], '5А', ['Математика', 'Чтение', 'Физкультура', 'История', 'Ин.язык'])]
        


teachers = [n_lib.Teacher('Косыгина', 'П.А.', 'Математика'),
            n_lib.Teacher('Продан', 'Н.Т.', 'Чтение'),
            n_lib.Teacher('Чуриков', 'В.М.', 'Физкультура'),
            n_lib.Teacher('Сурикова', 'И.К.', 'Ин.язык'),
            n_lib.Teacher('Праве', 'Е.В.', 'История')]

class_ids_raw = []
for i in kids:
    class_ids_raw.append(i.get_class_id())
class_ids = list(set(class_ids_raw))
print('1. Классы школы: ', class_ids)

class_id = '3А'
kids_list = []
kids_list_raw = []
for i in kids:
    kids_list_raw.append(i.get_class_kids_list())
for i in kids_list_raw:
    if i[1] == class_id:
        kids_list.append(i[0])
print(f'2. Ученики класса {class_id}: ', kids_list)

kid_full_name = 'Сидоров Л.Н.'
kid_subj = []
kid_subj_raw = []
for i in kids:
    kid_subj_raw.append(i.get_kid_subj_list())
for i in kid_subj_raw:
    if i[0] == kid_full_name:
        kid_subj.append(i[1])
print(f'3. Предметы ученика {kid_full_name}: ', kid_subj)

kid_full_name = 'Киренский А.В.'
kid_parent = []
kid_parent_raw = []
for i in kids:
    kid_parent_raw.append(i.get_parent_list())
for i in kid_parent_raw:
    if i[0] == kid_full_name:
        kid_parent.append(i[1])
print(f'4. Родители ученика {kid_full_name}: ', kid_parent)

class_id = '1А'
class_subj_list = []
class_subj_list_raw = []
teacher_list = []
teacher_list_raw = []
for i in kids:
    class_subj_list_raw.append(i.get_class_subj_list())
for i in class_subj_list_raw:
    if i[0] == class_id:
        class_subj_list.append(i[1])
        break
for i in teachers:
    teacher_list_raw.append(i.get_teachers_list())
for n in teacher_list_raw:
    for j in class_subj_list:
        for k in j:
            if n[1] == k:
                teacher_list.append(n[0])
print(f'5. Учителя класса {class_id}: ', teacher_list)













            
