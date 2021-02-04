"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’]
и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from _collections import deque

HEX_DICT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hex_mult_one(num1, num2):
    nums_mult = deque()
    if num2 == '0':
        return deque('0')
    saved = 0
    num2_dec = HEX_DICT[num2]
    while len(num1):
        res = HEX_DICT[num1.pop()] * num2_dec + saved
        # print(f'{res=}')
        saved = res // 0x10
        res %= 0x10
        # print(f'saving {saved}')
        nums_mult.append(list(HEX_DICT.keys())[res])
    nums_mult.append(list(HEX_DICT.keys())[saved])
    nums_mult.reverse()
    return nums_mult


def hex_sum(num1, num2):
    nums_sum = deque()
    saved = 0
    while len(num1) or len(num2):
        el1 = 0
        el2 = 0
        res = 0

        if len(num1):
            el1 = num1.pop()
            res += HEX_DICT[el1]

        if len(num2):
            el2 = num2.pop()
            res += HEX_DICT[el2]

        res += saved
        if res >= 16:
            saved = 1
            res -= 16
        else:
            saved = 0
        nums_sum.append(list(HEX_DICT.keys())[res])
    nums_sum.reverse()
    return nums_sum


def hex_mult(num1, num2):
    ret_deq = deque()
    deg = 0
    while len(num2):
        mult_num = num2.pop()
        print(f'Mult {num1} and {mult_num}')

        tmp_deq = hex_mult_one(num1.copy(), mult_num)

        for i in range(deg):
            tmp_deq.append('0')
        deg += 1
        print(f'{tmp_deq=}')
        ret_deq = hex_sum(ret_deq, tmp_deq)
    return ret_deq


num1_str = 'A2'
num2_str = 'C4F'

print(f'Сумма равна {hex_sum(deque(num1_str), deque(num2_str))}')

print(f'Произведение равно {hex_mult(deque(num1_str), deque(num2_str))}')


# print(f'Произведение 0xFABED и 0x1234 равно {hex_mult(deque("FABED"), deque("12345"))}')