from locale import currency
from numpy import true_divide


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            if item == self.tail.getData():
                self.tail = previous

            previous.setNext(current.getNext())

        self.length = self.length - 1

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

        self.length = self.length + 1

    def index(self, item):
        current = self.head
        count = 0
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count = count + 1

        if not found:
            return 'Not found'
        else:
            return count

    def pop(self):
        current = self.head
        previous = None
        last = False

        while not last:
            next = current.getNext()
            if next == None:
                last = True
            else:
                previous = current
                current = next

        if previous == None:
            self.head = None
        else:
            previous.setNext(current.getNext())

        self.length = self.length - 1

    def __str__(self):
        current = self.head
        strArr = ""
        while current != None:
            strArr = strArr + " ," + str(current.getData())
            current = current.getNext()
        return strArr


mylist = OrderedList()


mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.pop()
print(mylist.size())
