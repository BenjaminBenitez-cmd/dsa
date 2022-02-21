class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.back = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getBack(self):
        return self.back

    def setNext(self, newnext):
        self.next = newnext

    def setBack(self, newBack):
        self.back = newBack

    def setData(self, newdata):
        self.data = newdata


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)

        if self.head != None:
            self.head.setBack(temp)
        else:
            self.tail = temp

        temp.setNext(self.head)

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
            temp.setBack(self.tail)
            self.length = self.length + 1

    def insert(self, pos, item):
        current = self.head
        count = 0

        while count != pos:
            current = current.getNext()
            count = count + 1

        temp = Node(item)
        temp.setNext(current)

        previous = current.getBack()

        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setBack(previous)

        self.length = self.length + 1

    def remove(self, item):
        current = self.head
        found = False

        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if not found:
            return 'Not found'

        previous = current.getBack()

        if previous == None:
            self.head = current.getNext()
        else:
            if item == self.tail.getData():
                self.tail = previous

            previous.setNext(current.getNext())

        self.length = self.length - 1

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
        previous = self.tail.getBack()
        previous.setNext(self.tail.getNext())
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


myList = List()
myList.add(89)
myList.add(30)
myList.add(42)
myList.add(321)

myList.remove(42)

print(myList.size())
print(myList)
