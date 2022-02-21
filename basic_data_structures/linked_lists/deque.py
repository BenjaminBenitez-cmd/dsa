from basic_data_structures.linked_lists.linked_list import Node


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addFront(self, item):
        temp = Node(item)
        if self.head == None:
            self.tail = temp

        temp.setNext(self.head)
        self.head = temp
        self.length = self.length + 1

    def addRear(self, item):
        temp = Node(item)

        self.tail.setNext(temp)
        self.length = self.length + 1

    def removeFront(self):
        current = self.head.getData()
        next = self.head.getNext()

        self.head = next
        self.length = self.length - 1

        return current

    def removeRear(self):
        current = self.head
        previous = None
        last = False

        while current != None and not last:
            if current.getNext() == None:
                last = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = None
        else:
            previous.setNext(current.getNext())

        self.length = self.length - 1

        return current.getData()

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.length


myDeque = Deque()
myDeque.addFront(90)
myDeque.addFront(8)
myDeque.addFront(23)

print(myDeque.size())
