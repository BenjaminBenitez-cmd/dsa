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


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)

        if self.head == None:
            self.tail = temp

        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

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

    # Append method time complexity of O(N)
    # def append(self, item):
    #     current = self.head
    #     previous = None

    #     while current != None:
    #         previous = current
    #         current = current.getNext()

    #     temp = Node(item)
    #     previous.setNext(temp)

    # Append method time complexity O(1)
    # Accomplished by adding a tail instance variable
    # when adding new item if its the first add a
    def append(self, item):
        temp = Node(item)
        self.tail.setNext(temp)

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

    def __str__(self):
        current = self.head
        strArr = ""
        while current != None:
            strArr = strArr + " ," + str(current.getData())
            current = current.getNext()
        return strArr


mylist = UnorderedList()


mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.pop()
print(mylist)
