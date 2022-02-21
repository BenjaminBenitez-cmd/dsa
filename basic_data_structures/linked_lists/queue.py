
from basic_data_structures.linked_lists.linked_list import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
            self.length = self.length + 1
        else:
            self.tail.setNext(temp)
            self.length = self.length + 1

    def dequeue(self):
        current = self.head
        next = self.head.getNext()

        self.head = next
        self.length = self.length - 1
        return current.getData()

    def size(self):
        return self.length
