import timeit
import random


# def test1():
#     l = []
#     for i in range(1000):
#         l = l + [i]


# def test2():
#     l = []
#     for i in range(1000):
#         l.append(i)


# def test3():
#     l = [i for i in range(1000)]


# def test4():
#     l = list(range(1000))


# popzero = timeit.Timer("x.pop(0)",
#                        "from __main__ import x")
# popend = timeit.Timer("x.pop()",
#                       "from __main__ import x")
# print("pop(0)   pop()")

# for i in range(1000000, 100000001, 1000000):
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print("%15.5f, %15.5f" % (pz, pt))


# for i in range(1000, 1000001, 20000):
#     t = timeit.Timer("x[random.randrange(%d)]" %
#                      i, "from __main__ import random, x")
#     x = list(range(i))
#     lst_time = t.timeit(number=1000)

#     print("%d, %10.3f" % (i, lst_time))

# for i in range(1000, 1000001, 20000):
#     t = timeit.Timer("del x[random.randrange(%d)]" %
#                      i, "from __main__ import random, x")
#     x = list(range(i))
#     lst_time = t.timeit(number=1000)

#     print("%d, %10.3f" % (i, lst_time))
