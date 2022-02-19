from locale import currency
from list import Node


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        temp = Node(item)

        if self.head == None:
            self.tail = temp

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


myStack = Stack()
myStack.push(8)
myStack.push(90)
myStack.push(76)
myStack.push(3)


print(myStack.peak())
