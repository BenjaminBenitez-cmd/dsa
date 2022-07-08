import algorithms.bubblesort
import algorithms.insertionsort
import algorithms.mergesort
import algorithms.quicksort
import algorithms.selectionsort
import algorithms.shellsort
import algorithms.shortbubblesort

import random
import timeit


print("analysis of sorting algorithms")
n = 500
alist = [random.randrange(n) for i in range(n)]

# bubble sort
bs = timeit.Timer("algorithms.bubblesort.bubbleSort(alist)",
                  "from __main__ import algorithms, alist")
# selection sort
sls = timeit.Timer("algorithms.selectionsort.selectionSort(alist)",
                   "from __main__ import algorithms, alist")
# insertion sort
ins = timeit.Timer("algorithms.insertionsort.insertionSort(alist)",
                   "from __main__ import algorithms, alist")
# shell sort
shs = timeit.Timer("algorithms.shellsort.shellSort(alist)",
                   "from __main__ import algorithms, alist")
# merge sort
ms = timeit.Timer("algorithms.mergesort.mergeSort(alist)",
                  "from __main__ import algorithms, alist")
# quick sort
qs = timeit.Timer("algorithms.quicksort.quickSort(alist)",
                  "from __main__ import algorithms, alist")

bs_time = bs.timeit(number=1000)
ins_time = ins.timeit(number=1000)
sls_time = sls.timeit(number=1000)
shs_time = shs.timeit(number=1000)
ms_time = ms.timeit(number=1000)
qs_time = qs.timeit(number=1000)

print("bubble sort:", bs_time)
print("selection sort:", sls_time)
print("insertions sort:", ins_time)
print("shell sort:", shs_time)
print("merge sort:", ms_time)
print("quick sort", qs_time)
