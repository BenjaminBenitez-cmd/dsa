def reverselist(l):
    n = len(l)
    if n == 1:
        return l
    else:
        return l[n - 1:] + reverselist(l[:n - 1])


print(reverselist([1, 2, 3, 4]))
