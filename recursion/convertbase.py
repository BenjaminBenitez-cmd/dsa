def toStr(str, base):
    convertToString = "0123456789"
    if base in convertToString:
        return base
    else:
        return toStr(str // 2, base) + convertToString[str % base]


print(toStr(434, 10))
