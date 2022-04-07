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


def iterBinarySearch(alist, low, high, item):
    low = 0
    high = len(alist) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if alist[mid] < item:
            low = mid + 1

        elif alist[mid] > item:
            high = mid - 1
        else:
            return True

    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(iterBinarySearch(testlist, 0, 9, 11))
