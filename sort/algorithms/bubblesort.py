def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def cocktailSort(alist):
    n = len(alist)
    swapped = True
    start = 0
    end = n-1

    while(swapped == True):
        swapped = False

        for i in range(start, end):
            if(alist[i] > alist[i + 1]):
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swapped = True

        if(swapped == False):
            break

        swapped = False

        end = end - 1

        for i in range(end-1, start-1, -1):
            if(alist[i] > alist[i + 1]):
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swapped = True

        start = start + 1


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 55, 44, 20]
    cocktailSort(alist)
    print(alist)
