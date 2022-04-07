import timeit
import random

# TODO: Figure how to import these functions

# implemented high and low index values


def binarySearch(alist, low, high, item):
    if high >= low:

        midpoint = (high + low) // 2

        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return binarySearch(alist, low, midpoint - 1, item)
        else:
            return binarySearch(alist, midpoint + 1, high,  item)
    else:
        return False


def iterBinarySearch(alist, low, high, item):
    low = 0
    high = len(alist) - 1
    midpoint = 0

    while low <= high:
        midpoint = (high + low) // 2

        if alist[midpoint] < item:
            low = midpoint + 1

        elif alist[midpoint] > item:
            high = midpoint - 1
        else:
            return True

    return False


# testing with timeit
for i in range(1000, 100001, 20000):
    trbs = timeit.Timer("binarySearch(alist, low, high, x)",
                        "from __main__ import binarySearch, alist, low, high, x")
    tibs = timeit.Timer("iterBinarySearch(alist, low, high, x)",
                        "from __main__ import iterBinarySearch, alist, low, high, x")

    alist = list(range(i))
    x = random.randrange(i)

    low = 0
    high = len(alist) - 1

    trbs_time = trbs.timeit(number=1000)
    tibs_time = tibs.timeit(number=1000)

    print("Recursive Binary Search, Iterative Binary Search")
    print("%15.5f, %15.5f" % (trbs_time, tibs_time))

# Findings demonstrate that the iterative binary search is faster that the recursive implementation
