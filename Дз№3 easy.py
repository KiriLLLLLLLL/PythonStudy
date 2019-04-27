__author__ = 'Ермаченков Кирилл'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):

    multiplier = 10.0 ** ndigits
    return int (number*multiplier + 0.5) / multiplier


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):

    a = str(ticket_number)

    if len(a) != 6:
        return 'Мало цифр'
    else:
        firstNumbers = int(a[0]) + int(a[1]) + int(a[2])
        secondNumbers = int(a[3]) + int(a[4]) + int(a[5])
        if firstNumbers == secondNumbers:
            return 'Счастливый'
        else:
            return 'Не счастливый'



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436752))
