import timeit


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


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)

        if self.head == None:
            self.tail = temp

        self.head = temp
        self.length = self.length + 1

    def size(self):
        return self.length

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
            self.length = self.length + 1
        else:
            self.tail.setNext(temp)
            self.length = self.length + 1

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0

        while count != pos:
            previous = current
            current = current.getNext()
            count = count + 1

        temp = Node(item)
        temp.setNext(current)

        if previous == None:
            self.head = temp
        else:
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

        while current != None and not last:
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

    def slice(self, start, stop):
        current = self.head
        count = 0

        res = List()

        while count <= stop:
            if count >= start and count < stop:
                res.append(current.getData())

            current = current.getNext()
            count = count + 1

        return res

    def __str__(self):
        current = self.head
        strArr = "["
        while current != None:
            strArr = strArr + str(current.getData()) + " "
            current = current.getNext()

        strArr = strArr + "]"
        return strArr


class OrderedList(List):
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
