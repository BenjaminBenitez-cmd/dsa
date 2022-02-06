

class Queue:
    def __init__(self):
        self.items = []

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


class QueueReversed(Queue):

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


# q = Queue()
# q.enqueue(4)
# q.enqueue('Dog')
# q.enqueue(13)
# print(q.size())

q = QueueReversed()
q.enqueue(4)
q.enqueue('test')
q.dequeue()
print(q.size())
