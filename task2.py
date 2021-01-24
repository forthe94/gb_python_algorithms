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