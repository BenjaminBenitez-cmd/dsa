# Analysis of linked list implementation vs built in python list performance

import timeit
import basic_data_structures.linked_lists.linked_list as LinkedList


def test():
    linkedListAppend = timeit.Timer("xa.append(1)", "from __main__ import xa")
    pythonListAppend = timeit.Timer("ya.append(1)", "from __main__ import ya")
    linkedListPop = timeit.Timer("xp.pop()", "from __main__ import xp")
    pythonListPop = timeit.Timer("yp.pop()", "from __main__ import yp")

    for i in range(1000000, 1000000001, 1000000):
        xa = LinkedList.List()
        xa_time = linkedListAppend.timeit(number=1000)

        ya = list()
        ya_time = pythonListAppend.timeit(number=1000)

        xp = LinkedList.List()
        # manually populate the list
        for num in range(i):
            xp.append(num)
        xp_time = linkedListPop.timeit(number=1000)

        yp = list(range(i))
        yp_time = pythonListPop.timeit(number=1000)

        linkedListAvgTime = (xp_time + xa_time) / 2
        pythonListAvgTime = (yp_time + ya_time) / 2

        print("Linked List, Python built-in List")
        print("%15.5f, %15.5f" % (linkedListAvgTime, pythonListAvgTime))
