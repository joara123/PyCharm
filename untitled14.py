cnt = 0
astr = '{2 * { 3 + ( 4 - 5 ) * 6 + { 7 + ( 8- 9 ) // 10 } * 2 } + 3 }'
#astr1 = '{2 * { 3 + ( 4 - 5 ) * 6 + { 7 + ( 8- 9 ) // 10 } * 2 } +3 '

for i in astr:
    if i == '(':
        cnt+=1
    elif i == ')':
        cnt -= 1
    elif i == '{':
        cnt += 2
    elif i == '}':
        cnt -= 2
        
if cnt == 0:
    print("astr is OK")
else:
    print("astr is NOK")
