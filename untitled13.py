def check_vracket(text):
    stack=[]
    for idx, letter in enumerate(text):
        if letter == '(':
            stack.append(idx)
        elif letter == ')':
            if stack:
                stack.pop()
            else:
                stack.append(idx)
                return True
    return False

print(check_vracket('2.4 + 23/12 + (3.141592 * .21'))