"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""


def geom_prog(s, n):
    if n == 0:
        return 0
    else:
        return s + geom_prog(-s/2, n - 1)


num = int(input('Введите количество элементов '))

sum = 1
sum = geom_prog(sum, num)

print(sum)