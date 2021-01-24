"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def print_table(f, l, nlc):
    if f > l:
        pass
    else:
        print(f'{chr(f)}:{f}\t', end='')

        if nlc == 9:
            print('')
            nlc = 0
        print_table(f + 1, l, nlc + 1)


first_symbol = 32
last_symbol = 127
new_line_counter = 0

print_table(first_symbol, last_symbol, new_line_counter)
print()
