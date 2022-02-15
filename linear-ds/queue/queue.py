

import timeit


class Queue:
    def __init__(self, items):
        self.items = [] or items

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Queue implementing the front at the start of the list and the -
# rear at the end of the list


class QueueWithAppend(Queue):

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


# time1 is the first implementation of Queue where the enqueue method makes use
# of the insert which has a time complexity of O(n)
# time2 is the second implementation of Queue where the
# enqueue method makes use of the append method which has
# a time complexity of O(1)
# QueueTwo with makes use of append() and pop(0) is faster
# than the first Queue
for i in range(1000, 1000001, 2000):
    t = timeit.Timer("q.enqueue(%d)" % i, "from __main__ import q")
    td = timeit.Timer("q.dequeue()", "from __main__ import q")
    t2 = timeit.Timer("q2.enqueue(%d)" % i, "from __main__ import q2")
    t2d = timeit.Timer("q2.dequeue()", "from __main__ import q2")

    q = Queue(list(range(i)))
    q2 = QueueWithAppend(list(range(i)))

    time1 = t.timeit(number=1000)
    time1d = td.timeit(number=1000)
    time2 = t2.timeit(number=1000)
    time2d = t2d.timeit(number=1000)

    print("Queue, Queue with append")
    print("%d, %10.3f, %10.3f" %
          (i, ((time1 + time1d) / 2), ((time2 + time2d) / 2)))

# for i in range(1000, 1000001, 2000):
#     t = timeit.Timer("q.dequeue()", "from __main__ import q")
#     t2 = timeit.Timer("q2.dequeue()", "from __main__ import q2")

#     q = Queue(list(range(i)))
#     q2 = QueueWithAppend(list(range(i)))

#     time1 = t.timeit(number=1000)
#     time2 = t2.timeit(number=1000)

#     print("Dequeue, Dequeue with append")
#     print("%d, %10.3f, %10.3f" % (i, time1, time2))
