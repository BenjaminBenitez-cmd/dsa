def shellSort(alist, increment):
    sublistcount = len(alist)//increment
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        # print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // increment


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist, 2)
    print(alist)
