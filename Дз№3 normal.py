__author__ = 'Ермаченков Кирилл'


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fib1 = 1
    fib2 = 1
    res = []
    if n <= 2:
        
        res.append(fib1)
        res.append(fib2)
        return res

    res.append(fib1)
    res.append(fib2)
    while n <= m:
        fib1, fib2 = fib2, fib1 + fib2
        res.append(fib2)
        n += 1
    return res

print(fibonacci(3, 30))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

import random

def bubble(long):
    for i in range(n - 1):
        for ind in range(n - i - 1):
            if long[ind] > long[ind + 1]:
                big = long[ind]
                long[ind] = long[ind + 1]
                long[ind + 1] = big
      
    
a = []
n = int(input("Длинна списка? "))
i = 0
while i < n:
    b = a.append(random.randint(0, 100))
    i += 1
print(a)
bubble(a)
print(a)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def new_filter (f, x):
    result = []
    for i in x:
        if f(i):
            result.append(i)
    return set(result)

print(list(new_filter(lambda x: x > 5, [29, 5, 23, -46, 457, 21, -4, 86, 3])))
    



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and 
       abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False






#Списал с разбора домашнего задания 3 и 4 задачи. Сам додуматься не смог(((

















