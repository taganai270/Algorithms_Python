"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
   ● Без использования алгоритма"решето Эратосфена";
   ● Использовать алгоритм "решето Эратосфена"
"""

import cProfile


def prime_num(n):
    lst = []
    k = 0

    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0

    return lst


# решето Эратосфена
def eratosthen(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
        a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b


cProfile.run('prime_num(3000)')
cProfile.run('eratosthen(3000)')

"""
 1.Без использования алгоритма:
             
        434 function calls in 0.644 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.644    0.644 <string>:1(<module>)
        1    0.644    0.644    0.644    0.644 homework_4-2.py:10(prime_num)
        1    0.000    0.000    0.644    0.644 {built-in method builtins.exec}
      430    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


 
 2. С использованием алгоритма "решето Эратосфена"
 
       434 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.003    0.003    0.003    0.003 homework_4-2.py:27(eratosthen)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      430    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


С использованием алгоритма "решето Эратосфена" время вычислений уменьшается. 
"""
