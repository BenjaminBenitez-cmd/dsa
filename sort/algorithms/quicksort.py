import algorithms.insertionsort


def quickSort(alist, partitionlimit):
    quickSortHelper(alist, 0, len(alist) - 1, partitionlimit)


def quickSortHelper(alist, first, last, partitionlimit):
    if first < last:
        splitpoint = partition(alist, first, last)

        # if length of partition is small enough perform insertion sort
        if (last - first + 1) < partitionlimit:
            algorithms.insertionsort.insertionSort(alist)
        else:
            quickSortHelper(alist, first, splitpoint - 1, partitionlimit)
            quickSortHelper(alist, splitpoint + 1, last, partitionlimit)


def findMedian(alist, first, last):
    mid = (last - first) // 2

    newarr = [alist[first], alist[mid], alist[last]]
    algorithms.insertionsort.insertionSort(newarr)
    return newarr[1]


def partition(alist, first, last):
    # use median of three to find pivot
    pivotvalue = findMedian(alist, first, last)
    leftmark = first + 1
    rightmark = last

    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(findMedian(alist, 0, 8))
