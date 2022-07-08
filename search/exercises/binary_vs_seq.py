import timeit
import random

# TODO: Figure how to import these functions


def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)


def sequentialSearch(alist, item):
    found = False

    for i in alist:
        if i == item:
            found = True

        if found == True:
            return True

    return found


# testing with timeit
for i in range(1000, 100001, 20000):
    tbs = timeit.Timer("binarySearch(alist, x)",
                       "from __main__ import binarySearch, x, alist")
    tss = timeit.Timer("sequentialSearch(alist, x)",
                       "from __main__ import sequentialSearch, x, alist")

    alist = list(range(i))
    x = random.randrange(i)

    tbs_time = tbs.timeit(number=1000)
    tss_time = tss.timeit(number=1000)

    print("Binary Search, Sequential Search")
    print("%15.5f, %15.5f" % (tbs_time, tss_time))


# Binary search appears to average out faster speeds than the sequential search
