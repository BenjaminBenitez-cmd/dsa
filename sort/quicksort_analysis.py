import algorithms.quicksort
import timeit
import random

qs = timeit.Timer("algorithms.quicksort.quickSort(alist, i)",
                  "from __main__ import algorithms, alist, i")
n = 500
alist = [random.randrange(n) for i in range(n)]

for i in range(100, 400, 100):
    qs_time = qs.timeit(number=1000)

    print("Interval: ", i, "Time: ", qs_time)
