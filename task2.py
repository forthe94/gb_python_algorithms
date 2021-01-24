"""
https://drive.google.com/file/d/1S89m85BEBWtPLzWD1tpxRhjX6I7VOjie/view?usp=sharing
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

def count(e, o, num):
    if num == 0:
        pass
    else:
        if num % 2 == 0:
            e = e + 1
        else:
            o = o + 1
        num = num // 10

        e, o, num = count(e, o, num)
    return e, o, num


number = int(input('Введите число '))

even = 0
odd = 0
even, odd, number = count(even, odd, number)

print(f'Количество чётных цифр - {even}, количество нечетных - {odd}.')