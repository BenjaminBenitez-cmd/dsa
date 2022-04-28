import algorithms.shellsort

import timeit
import random

print("analysis of shell sort algorithms")
n = 500
alist = [random.randrange(n) for i in range(n)]


for i in range(2, 4):
    shs = timeit.Timer("algorithms.shellsort.shellSort(alist, i)",
                       "from __main__ import algorithms, alist, i")
    shs_time = shs.timeit(number=1000)

    print('Shell sort:', shs_time, "increment: ", i)
