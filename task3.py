"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def reverse(n, depth, dc):
    if n == 0:
        pass
    else:
        saved = n % 10
        depth = depth + 1
        dc = dc + 1
        n = n // 10
        n, depth, dc = reverse(n, depth, dc)
        n = n + saved * pow(10, (dc - depth))
        depth = depth - 1
    return n, depth, dc


num = int(input('Введите число '))

dep = 0
digit_count = 0


num, dep, digit_count = reverse(num, dep, digit_count)

print(num)