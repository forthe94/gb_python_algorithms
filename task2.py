from timeit import timeit
from cProfile import run

"""
Вывод:
При наивной реализации проверки простоты числа получается квардратичная зависимость(цилк в цикле). 
У решета Эратосфена зависимость линейная.
"""


def eratosthenes_sieve(n):
    s = [i for i in range(n)]
    s[1] = 0

    for i in range(2, n):
        if s[i] != 0:
            j = i + i
            while j < n:
                s[j] = 0
                j += i
    return s


def naive_prime_number_check(n):
    s = [i for i in range(n)]
    all_numbers = [i for i in range(n)]
    s[1] = 0

    for cur in range(n):
        for item in all_numbers[2:cur//2 + 1]:
            if s[cur] % item == 0:
                s[cur] = 0
                break
    return s


sieve = naive_prime_number_check(32)
print([i for i in sieve if i != 0])

sieve = eratosthenes_sieve(32)
print([i for i in sieve if i != 0])

print(timeit('naive_prime_number_check(10)', number=100, globals=globals()))   # 0.00030312599847093225
print(timeit('naive_prime_number_check(100)', number=100, globals=globals()))   # 0.006190290994709358
print(timeit('naive_prime_number_check(1000)', number=100, globals=globals()))   # 0.2666888020175975
print(timeit('naive_prime_number_check(10000)', number=100, globals=globals()))  # 22.68130555000971

run('naive_prime_number_check(10000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.230    0.230 <string>:1(<module>)
#         1    0.229    0.229    0.230    0.230 task2.py:18(naive_prime_number_check)
#         1    0.000    0.000    0.000    0.000 task2.py:19(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task2.py:20(<listcomp>)
#         1    0.000    0.000    0.230    0.230 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit('eratosthenes_sieve(10)', number=100, globals=globals()))   # 0.0001562819816172123
print(timeit('eratosthenes_sieve(100)', number=100, globals=globals()))   # 0.0015399859985336661
print(timeit('eratosthenes_sieve(1000)', number=100, globals=globals()))   # 0.020675753999967128
print(timeit('eratosthenes_sieve(10000)', number=100, globals=globals()))  # 0.24413564099813811

run('eratosthenes_sieve(10000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 task2.py:5(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 task2.py:6(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}