from xml.etree.ElementPath import ops
from pythonds.basic import Stack


def toPostfix(infixexpr):
    prec = {}
    prec['**'] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()

            while topToken != '(' and not opStack.isEmpty():
                postfixList.append(topToken)
                topToken = opStack.pop()

                if topToken != '(' and opStack.isEmpty():
                    return 'Error in the expression'

        elif token in ['**', '*', '/', '+', '-', '(']:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
        else:
            return 'Error in the expression'

    while not opStack.isEmpty():
        topToken = opStack.pop()

        if topToken == '(':
            return 'Error in the expression'

        postfixList.append(topToken)

    return " ".join(postfixList)


print(toPostfix("( A + B ) * ( C + D ) * ( E + F )"))
print(toPostfix("A + ( ( B + C ) * ( D + E ) )"))
print(toPostfix("A  * B * C * D + E + F"))
