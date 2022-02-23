def reversestr(item):
    n = len(item)
    if item == '':
        return item
    else:
        return item[n - 1] + reversestr(item[:n - 1])
        

print(reversestr('hello'))
