import timeit
import random

from numpy import number


def recfib(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    else:
        return recfib(n - 1) + recfib(n - 2)


def iterfib(n):
    a = 0
    b = 1
    count = 0
    if n < 2:
        return 1

    while n >= 2:
        count = a + b
        a = b
        b = count

        n = n - 1

    return count


testrecfib = timeit.Timer("recfib(x)", "from __main__ import recfib, x")
testiterfib = timeit.Timer("iterfib(x)", "from __main__ import iterfib, x")


# The recursive function of fib is slower than the iterative version
if __name__ == "__main__":
    for i in range(10, 1000, 5):
        x = random.randrange(i)
        timerec = testrecfib.timeit(number=1000)
        timeiter = testiterfib.timeit(number=1000)
        print("Recursive fib, Iterative fib")
        print("%15.5f, %15.5f" % (timerec, timeiter))
