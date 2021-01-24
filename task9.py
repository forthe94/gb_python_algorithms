"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def count_digit_sum(num):
    sum = 0
    while not num == 0:
        sum = sum + num % 10
        num = num // 10
    return sum


print('Вводите числа через enter, как закончите введите пустой enter')
saved_sum = 0
n = 0
while True:
    a = input()
    if a == '':
        break
    n = n + 1
    a = int(a)
    tmp_sum = count_digit_sum(a)
    if tmp_sum > saved_sum:
        saved_sum = tmp_sum
        saved_num = n

print(saved_sum, saved_num)