from random import random
import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        if branchLen < 15:
            t.color("lightgreen")
        else:
            t.color("green")
        r = random.randrange(15, 40)
        rl = random.randrange(10, 15)
        t.width(branchLen // 20)
        t.forward(branchLen)
        t.right(r)
        tree(branchLen-rl, t)
        t.left(r*2)
        tree(branchLen-rl, t)
        t.right(r)
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
