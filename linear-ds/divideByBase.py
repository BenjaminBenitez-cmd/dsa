from pythonds.basic import Stack


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()
    if decNumber == base:
        return '10'
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


print(baseConverter(16, 16))
