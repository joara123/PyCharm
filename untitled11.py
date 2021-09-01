import sys
input = sys.stdin.readline

def solve(string):
    
    stack = []
    for ch in string:
        if len(stack) == 0 and ch == ')' :
            return 'No'
        
        if ch == '(':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'No'
    if len(stack) == 0:
        return 'Yes'
    return 'No'
    
if _name_ == "_main_":
    n = int(input().strip())
    for i in range(n):
        string = input().strip()
        print(solve(string))