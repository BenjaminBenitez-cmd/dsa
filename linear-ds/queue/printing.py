import random
from pythonds.basic import Queue

# Computer lab printing simulation, in this task
# At what rate should our printer print in order for students to finish before time
#  How would you modify the printer simulation to reflect a large number of students?
# Answer: I would change the way to calculate probability
# Change the code to reflect the amount of average print tasks by half
# change the code to parametize the number of students in a simultation


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

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

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


class Task:
    def __init__(self, time, avgPages):
        self.timestamp = time
        self.pages = random.randrange(1, avgPages + 1)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute, numStudents, avgTasks):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    frequency = 2

    endRange = (numSeconds // (numStudents * frequency))

    for currentSecond in range(numSeconds):

        if newPrintTask(endRange):
            task = Task(currentSecond, avgTasks)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %
          (averageWait, printQueue.size()))


def newPrintTask(endRange):

    num = random.randrange(1, endRange + 1)
    if num == endRange:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 10, 10, 20)
