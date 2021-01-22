"""
https://drive.google.com/file/d/1ltHt9Gw1HA2DwMHMT5iNBUQVBQbsm6No/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""

a = int(input('Введите целое трёхзначное число: '))
s = a % 10
p = a % 10

a = a // 10

s = s + a % 10
p = p * (a % 10)

a = a // 10

s = s + a % 10
p = p * (a % 10)

print(f'Сумма цифр введенного числа равна {s}')
print(f'Произведение цифр введенного числа равно {p}')
