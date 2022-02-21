import time


def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    end = time.time()

    print(end - start)
    return theSum, end - start


sumOfN2(100000000)
