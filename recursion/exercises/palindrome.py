from typing import Deque

from pythonds.basic import Queue


def cleaner(item):
    s = ""

    for i in item:
        if not i in [" ", "-", ";", "’", ",", "."]:
            s = s + i.lower()

    print(s)
    return s


def palindrome(item):
    item = cleaner(item)
    n = len(item)
    isPal = True

    if n <= 1:
        return True

    if item[n - 1] == item[0]:
        return palindrome(item[1:n - 1])
    else:
        isPal = False

    if isPal == False:
        return False


print(palindrome('civvic'))
