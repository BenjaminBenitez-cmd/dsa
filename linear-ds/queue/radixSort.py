from json.tool import main
from pythonds.basic import Queue

# # Naive implementation


def sort(nums):
    mainBin = Queue()
    bins = []
    maxNum = len(str(max(nums)))

    # create bins from 1 to 9
    for i in range(10):
        newQueue = Queue()
        bins.append(newQueue)

    # convert to string and add 0 to match with highest
    for i in nums:
        numStr = str(i)

        if len(numStr) < maxNum:
            while len(numStr) != maxNum:
                numStr = '0' + numStr

        mainBin.enqueue(numStr)

    count = maxNum - 1

    while count >= 0:
        while not mainBin.isEmpty():
            num = mainBin.dequeue()
            bins[int(num[count])].enqueue(num)

        for i in bins:
            while not i.isEmpty():
                mainBin.enqueue(i.dequeue())

        count = count - 1

    print('Smallest to largest')
    while not mainBin.isEmpty():
        print(int(mainBin.dequeue()))


sort([100, 50, 80, 39, 10, 8])
