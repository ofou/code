def reverseInParentheses(inputString):
    stack = []
    temp = ''
    for index, letter in enumerate(inputString):
        if (letter == '('):
            stack.append(temp)
            temp = ''
        elif (letter == ')'):
            temp = stack.pop() + temp[::-1]
        else:
            temp += letter
    if not temp == '':
        stack.append(temp)
    return ''.join(stack)