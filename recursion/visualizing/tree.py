from random import random
import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        len = random.randrange(1, 15)
        t.forward(branchLen)
        t.right(random.randrange(15, 45))
        tree(branchLen-len, t)
        t.left(random.randrange(15, 45))
        tree(branchLen-len, t)
        t.right(random.randrange(15, 45))
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()


main()
