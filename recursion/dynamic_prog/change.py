from math import remainder


def getchange(amount, change, coins):
    for i in coins:

        while(amount >= coins[i]):
            amount = amount - coins[i]
            change.append(coins[i])

    return change

# Inefficient recursive solution to change problem


def recMC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

    return minCoins


if __name__ == '__main__':
    print(recMC([10, 5, 25, 1], 63, [0]*64))
