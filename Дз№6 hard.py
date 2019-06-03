__author__ = 'Ермаченков Кирилл'

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Worker:
    def __init__(self, name, surname, salary, position, base):
        self.name = name
        self.surname = surname
        self.salary = float(salary)
        self.position = position
        self.base = float(base)
        self.hours = None
        self.income = None

    def payroll(self, hours):
        self.hours = hours
        if hours > self.base:
            self.income = self.salary * (1 + 2 * (hours / self.base - 1))
        else:
            self.income = self.salary * (hours / self.base)

def op_f(way):
    with open(os.path.join(way), 'r', encoding='UTF-8') as f:
        return f.readlines()

workers = op_f('workers.txt')
hours = op_f('hours.txt')
ws = {}
for worker in workers[1:]:
    worker = worker.split()
    ws[f'{worker[1]} {worker[0]}'] = Worker(*worker)

for h in hours[1:]:
    h = h.split()
    ws[f'{h[1]} {h[0]}'].payroll(float(h[2]))

for worker in sorted(ws.keys()):
    print(f'{ws[worker].position} {worker} с окладом {ws[worker].salary} руб. за {ws[worker].base} часов,',
          f'отработал {ws[worker].hours} часови заработал {round(ws[worker].income, 2)} руб.')










    
