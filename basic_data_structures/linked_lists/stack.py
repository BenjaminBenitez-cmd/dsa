from basic_data_structures.linked_lists.linked_list import Node
import timeit


class ListStack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        temp = Node(item)

        temp.setNext(self.head)
        self.head = temp
        self.length = self.length + 1

    def peak(self):
        return self.head.getData()

    def size(self):
        return self.length

    def pop(self):
        current = self.head
        next = self.head.getNext()

        self.head = next
        self.length = self.length - 1
        return current


# Performance between a list based Stack and a linked list based Stack

linkedListPush = timeit.Timer("xa.push(1)", "from __main__ import xa")
pythonListPush = timeit.Timer("ya.push(1)", "from __main__ import ya")
linkedListPop = timeit.Timer("xp.pop()", "from __main__ import xp")
pythonListPop = timeit.Timer("yp.pop()", "from __main__ import yp")

for i in range(1000000, 1000000001, 1000000):
    xa = Stack()
    xa_time = linkedListPush.timeit(number=1000)

    ya = ListStack()
    ya_time = pythonListPush.timeit(number=1000)

    xp = Stack()
    # manually populate the stack
    for num in range(i):
        xp.push(num)
    xp_time = linkedListPop.timeit(number=1000)

    yp = ListStack()
    for num in range(i):
        yp.push(num)
    yp_time = pythonListPop.timeit(number=1000)

    linkedListAvgTime = (xp_time + xa_time) / 2
    pythonListAvgTime = (yp_time + ya_time) / 2
    print("Linked List Queue, List based Queue")
    print("%15.5f, %15.5f" % (linkedListAvgTime, pythonListAvgTime))
