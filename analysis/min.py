
from random import randrange
import time


# def findMin(alist):
#     overallmin = alist[0]
#     for i in alist:
#         if i < overallmin:
#             overallmin = i
#     return overallmin

def findMin(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar


for listSize in range(1000, 10001, 1000):
    print(listSize)
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print("Size: %d time: %f" % (listSize, end - start))


print(findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
