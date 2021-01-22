"""
https://drive.google.com/file/d/1ltHt9Gw1HA2DwMHMT5iNBUQVBQbsm6No/view?usp=sharing
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

a = input('Введите первую букву ')
b = input('Введите вторую букву ')

a = ord(a) - 96
b = ord(b) - 96
letters_count = a - b

if letters_count < 0:
    letters_count = -letters_count

print(f'Вы ввели буквы находящиеся на местах {a}, {b} в алфавите и между ними {letters_count} букв')