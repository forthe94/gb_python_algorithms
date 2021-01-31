"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

Вывод: рекурсия и цикл показали линейную сложность(время выполнения увеличивалось в 2 раза при увеличении в 2 раза n).
У рекурсии не число внутренних вызовов возрастало пропорционально n, поэтому время выполнения не начало сильно расти.
Ну и конечно победила математическая реализация, которая считала сумму за константное время
"""


from timeit import timeit
from cProfile import run


def geom_prog_rec(s, n):
    # Рекурсия
    if n == 0:
        return 0
    else:
        return s + geom_prog_rec(-s/2, n - 1)


def geom_prog_cycle(n, start=1, step=-0.5):
    # цикл
    s = 0
    cur = 1
    for i in range(n):
        s += cur
        cur *= step
    return s


def geom_prog_math(n):
    # математический подход!
    return 1 * (1 - (-0.5) ** n) / (1 - (-0.5))

rec_sum = 1

print(timeit('geom_prog_rec(rec_sum, 16)', number=100, globals=globals()))   # 0.00023033301113173366
print(timeit('geom_prog_rec(rec_sum, 32)', number=100, globals=globals()))   # 0.00043728097807615995
print(timeit('geom_prog_rec(rec_sum, 64)', number=100, globals=globals()))   # 0.0009384420118294656
print(timeit('geom_prog_rec(rec_sum, 128)', number=100, globals=globals()))  # 0.0018600359908305109

run('geom_prog_rec(rec_sum, 128)')

# 132 function calls (4 primitive calls) in 0.000 seconds

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     129/1    0.000    0.000    0.000    0.000 task1.py:8(geom_prog_rec)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('')

print(timeit('geom_prog_cycle(16)', number=100, globals=globals()))   # 0.00010350102093070745
print(timeit('geom_prog_cycle(32)', number=100, globals=globals()))   # 0.000168478989508003
print(timeit('geom_prog_cycle(64)', number=100, globals=globals()))   # 0.0003058139991480857
print(timeit('geom_prog_cycle(128)', number=100, globals=globals()))  # 0.0006369460024870932
print(timeit('geom_prog_cycle(256)', number=100, globals=globals()))  # 0.001169989991467446


run('geom_prog_cycle(128)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:16(geom_prog_cycle)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# print('')
#
print(timeit('geom_prog_math(16)', number=100, globals=globals()))   # 5.8819015976041555e-05
print(timeit('geom_prog_math(256)', number=100, globals=globals()))  # 3.431900404393673e-05
print(timeit('geom_prog_math(1024)', number=100, globals=globals()))  # 4.188701859675348e-05

run('geom_prog_math(128)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:26(geom_prog_math)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}