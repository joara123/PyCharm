text = '2.4 + 23/12 + (3.141592 * .21'

text1 = 't.4 + (32*1) + 1'

stack = []

for i,j in enumerate(text):
    if j == '(':
        stack.append(i)
    elif j == ')':
        if stack:
            stack.pop()
        else:
            stack.append(i)
            print(stack)
print(stack)