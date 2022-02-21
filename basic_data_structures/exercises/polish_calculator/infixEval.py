from infixToPost import toPostfix
from postfixEval import postEval


def infixEval(infixStr):
    postFix = toPostfix(infixStr)
    result = postEval(postFix)

    return result


print(infixEval('5 * 3 ** ( 4 - 2 )'))
