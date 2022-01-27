from heapq import merge
import timeit

# Bubble sort algorithm


def bubbleSort(arr, k):
    for i in range(k):
        isFound = True
        for j in range(k - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                isFound = False

        if isFound == True:
            break

    return arr

# Merge sort algorithm


def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of an array
        mid = len(arr) // 2
        # Dividing the array of elements
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


def linearSort(arr, k):
    if(len(arr) < 1):
        return arr

    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

    return smallest


def logLinSort(arr, k):
    if(len(arr) < 1):
        return arr
    arr[:k]
    arr = mergeSort(arr)
    return arr[0]


sL = timeit.Timer("linearSort(x, k)",
                  "from __main__ import x, k, linearSort")

sLL = timeit.Timer("logLinSort(x, k)",
                   "from __main__ import x, k, logLinSort")

for i in range(1000, 1000001, 20000):
    x = list(range(i))
    k = len(x)
    smLin = sL.timeit(number=1000)
    smLogLin = sLL.timeit(number=1000)
    print("Linear, Log Linear")
    print("%15.5f, %15.5f" % (smLin, smLogLin))


# to make the previous algorithm to be linear we had to change the implementation to store the smallest number at any given point in time
