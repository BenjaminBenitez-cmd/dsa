import random


def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res


def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1
    return numSame / len(goal)


def main():
    goalstring = "methinks it is like a weasel"
    newstring = generateOne(28)
    best = 0
    count = 0
    newScore = score(goalstring, newstring)
    while newScore < 1:
        if count % 1000000 == 0:
            print('The best score: ', best)
        if newScore > best:
            best = newScore
        newstring = generateOne(28)
        newScore = score(goalstring, newstring)
        count = count + 1
        print(count)


main()
