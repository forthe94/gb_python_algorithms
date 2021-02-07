"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
import sys

mem_used = 0


def reverse(n, depth, dc):
    if n == 0:
        pass
    else:
        # При  каждом погружении в рекурсию создаются доп переменные.
        # Будем считать сколько памяти они кушают
        saved = n % 10
        depth = depth + 1
        dc = dc + 1
        n = n // 10
        global mem_used
        mem_used += sys.getsizeof(saved) + sys.getsizeof(dc)\
            + sys.getsizeof(n) + sys.getsizeof(depth)
        n, depth, dc = reverse(n, depth, dc)
        n = n + saved * pow(10, (dc - depth))
        depth = depth - 1
    return n, depth, dc


num = 123456789

dep = 0
digit_count = 0
print(f'Reversing {num} recursive')

num, dep, digit_count = reverse(num, dep, digit_count)
print(f'{mem_used=}') # mem_used=1004

print(num)

num = 123456789
print(f'Reversing {num} with string operations')

# вариант 2, со строками
# получается каждый раз создается новый объект,
# попробую расписать это в коде
mem_used = 0
num = str(num)
result = ''
for i in num:
    tmp_result = i + result
    mem_used += sys.getsizeof(i)
    mem_used += sys.getsizeof(result)
    mem_used += sys.getsizeof(tmp_result)
    result = tmp_result

print(f'{mem_used=}') # mem_used=1413
print(result)


BASE = 10
# Человеческий вариант с целыми числами
num = 123456789
print(f'Reversing {num} with int operations')
mem_used = 0
result = 0
mem_used += sys.getsizeof(result)
mem_used += sys.getsizeof(BASE)
mem_used += sys.getsizeof(num)
while num > 0:
    result = result * BASE + num % BASE
    num = num // BASE
print(f'{mem_used=}') # mem_used=80
print(result)
"""
Вывод:
Решения с рекурсией съело много памяти (я думаю примерно столько же сколько со строками,
если учитывать расход памяти на записи в стек при рекурсивных вызовах), решение со строками
тоже. По сравнению с решением через операции с целыми числами первые два решения потратили
абсолютно ненормальное количество памяти.         
Версия питона - 3.9.1. 
Linux 4.15.0-55-generic #60~16.04.2-Ubuntu SMP x86_64 GNU/Linux                                 
"""