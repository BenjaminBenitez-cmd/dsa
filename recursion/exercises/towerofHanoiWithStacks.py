from re import A
from pythonds.basic import Stack
import sys


def moveDisksBetweenTwoPoles(src, dest, s, d):
    pole1TopDisk = src.pop()
    pole2TopDisk = src.pop()

    if(pole1TopDisk == -sys.maxsize):
        src.push(pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
    elif pole2TopDisk == -sys.maxsize:
        src.push(pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)
    elif (pole1TopDisk > pole2TopDisk):
        src.push(pole1TopDisk)
        src.push(pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
    else:
        dest.push(pole2TopDisk)
        dest.push(pole1TopDisk)
        moveDisk(d, s, pole2TopDisk)


def moveDisk(fromPeg, toPeg, disk):
    print("Move the disk", disk, "from '", fromPeg, "' to '", toPeg, "'")


def tohIterative(num_of_disks, src, aux, dest):
    s, d, a = "S", "D", "A"

    if (num_of_disks % 2 == 0):
        temp = d
        d = a
        a = temp

    total_num_of_moves = int(pow(2, num_of_disks) - 1)

    for i in range(num_of_disks, 0, -1):
        src.push(i)

    for i in range(1, total_num_of_moves + 1):
        if (i % 3 == 1):
            moveDisksBetweenTwoPoles(src, dest, s, d)

        elif (i % 3 == 2):
            moveDisksBetweenTwoPoles(src, aux, s, a)

        elif (i % 3 == 0):
            moveDisksBetweenTwoPoles(aux, dest, a, d)


num_of_disks = 3

src = Stack()
dest = Stack()
aux = Stack()

tohIterative(num_of_disks, src, aux, dest)
