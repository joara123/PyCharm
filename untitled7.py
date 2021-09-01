while True:
    str = input("문자열 입력: ")
    if str=='':
        break;
    
    chlist=[]
    for i in range(len(str)):
        chlist.append(str[i])
    print('chlist=',chlist)
    
    count = 0
    candi=''
    
    for i in range(len(str)):
        if count == 0:
            candi = chlist[i]
            count=1
        elif candi == chlist[i]:
            count += 1
        else:
            count -=1
            
    if count == 0:
        print("과반수 넘는 문자 없음")
        continue
    
    count = 0
    for i in range(len(chlist)):
        if candi == chlist[i]:
            count+=1
    if (count > len(chlist) // 2):
        print("과반수 넘는 문자: ",candi)
    else:
        print("과반수 넘는 문자 없음")