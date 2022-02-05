from pythonds.basic import Stack


def infixToPostFixConverter(infixStr):
    opstack = Stack()
    output = []
    inflix = infixStr.split()
    inflixLength = len(inflix)

    for i in range(inflixLength):
        if inflix[i] in ['A', 'B', 'C']:
            output.append(inflix[i])
        elif inflix[i] == '(':
            opstack.push(inflix[i])
        elif inflix[i] == ')':
            top = opstack.peek()
            while top != '(':
                item = opstack.pop()
                output.append(item)
                top = opstack.peek()

            opstack.pop()
        elif inflix[i] in ['*', '/', '+', '-']:
            top = opstack.peek()
            while top != '(':
                item = opstack.pop()
                output.append(item)
                top = opstack.peek()

            opstack.push(inflix[i])

    while not opstack.isEmpty():
        item = opstack.pop()
        if item in ['*', '/', '+', '-']:
            output.append(item)

    return output


print(infixToPostFixConverter('( A + ( B * C ) )'))
