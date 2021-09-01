data = [[21,7,43,65],[2,8,72,52]]

while True:
    search = input("찾을 값: ")
    
    if not(search.isdigit()):
        print("숫자 아님")
        continue
    
    search = int(search)
    notfound = True
    
    for i in range(len(data)):
        if search in data[i]:
            print("위치",i,",",data[i].index(search))
            notfound = False
            
    if(notfound):
        print("찾지 못함")
        break
        