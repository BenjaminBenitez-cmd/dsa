import random
from pythonds.basic import Queue

# Bank teller simulation
# A bank can have around 20 customers lined up per hour. Each customer
# may have different issues they want addressed. Here are the most common
# issues and the time they may take on average
# 1. Account creation / deletion = 20 mins %30
# 2. General Information = 5 mins %60
# 3. Misc = 1 min %10
# The bank wants to know if a single teller would be to handle this frequency


class Teller:
    def __init__(self):
        self.currentTask = None
        self.timeRemaining = 0
        self.amount = 4

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask
        # get time based on type of task
        self.timeRemaining = newTask.taskTime() * 60/self.amount


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.probailities = [1, 2, 2, 2, 3, 3, 3, 3, 3, 3]

    def getStamp(self):
        return self.timestamp

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

    def taskTime(self):
        timeMap = {1: 1, 2: 20, 3: 5}
        randomnum = random.randrange(0, 10)
        return timeMap[self.probailities[randomnum]]


def simulation(numSeconds, numCustomers):
    teller = Teller()
    tellerQueue = Queue()

    waitingtimes = []

    endRange = numSeconds // numCustomers
    for currentSecond in range(numSeconds):

        if newPrintTask(endRange):
            task = Task(currentSecond)
            tellerQueue.enqueue(task)

        if (not teller.busy()) and (not tellerQueue.isEmpty()):
            nexttask = tellerQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            teller.startNext(nexttask)

        teller.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %
          (averageWait, tellerQueue.size()))


def newPrintTask(endRange):

    num = random.randrange(1, endRange + 1)
    if num == endRange:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 20)

# The simulation reveals that a single teller would definately be
# unable to take care of all the customers efficiently, the bank
# would need at least 5 tellers
