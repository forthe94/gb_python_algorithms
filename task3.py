"""
https://drive.google.com/file/d/1ltHt9Gw1HA2DwMHMT5iNBUQVBQbsm6No/view?usp=sharing
По введенным пользователем координатам двух точек
вывести уравнение прямой вида y = kx + b,
проходящей через эти точки.
"""

print('Ввведите координаты первой точки')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))


print('Ввведите координаты второй точки')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

k = (y2 - y1)/(x2 - x1)

b = (x2*y1 - x1 * y2) / (x2 - x1)

print(f'Получившееся уравнение прямой y = {k:2}x + {b:2}')