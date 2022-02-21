from infixEval import infixEval


def calculator():
    print('---------Infix Evaluator ----------')
    print('Eg. 8 + 3 * ( 5 * 3 )')
    exp = input('Enter your infix expression: ')

    result = infixEval(exp)
    print('Answer: ', result)


calculator()
