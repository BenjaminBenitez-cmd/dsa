from pythonds.basic import Stack
import operator


def postEval(postfixstr):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    operandStack = Stack()
    tokenList = postfixstr.split()

    for token in tokenList:
        if token in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            operandStack.push(int(token))
        else:
            op_fun = ops[token]
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = op_fun(operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


print(postEval('7 8 + 3 2 + /'))
