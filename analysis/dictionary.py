import timeit
import random

# # contain test
# for i in range(1000, 1000001, 20000):
#     t = timeit.Timer("random.randrange(%d) in x" %
#                      i, "from __main__ import random, x")

#     x = list(range(i))
#     lst_time = t.timeit(number=1000)

#     x = {j: None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))

# get test
# for i in range(1000, 1000001, 20000):
#     t = timeit.Timer("x.get(random.randrange(%d))" %
#                      i, "from __main__ import random, x")

#     x = {j: None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     print("%d, %10.3f" % (i, lst_time))

# set test
# for i in range(1000, 1000001, 20000):
#     t = timeit.Timer("x[random.randrange(%d)] = 'x'" %
#                      i, "from __main__ import random, x")

#     x = {j: None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     print("%d, %10.3f" % (i, lst_time))

# set test
for i in range(1000, 1000001, 20000):
    t = timeit.Timer("del x[rd]", "from __main__ import x, rd")

    x = {j: None for j in range(i)}
    rd = random.randrange(i)
    d_time = t.timeit(number=1000)
    print("%d, %10.3f" % (i, d_time))
