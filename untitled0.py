data = [[21, 7, 43, 65], [2, 8, 72, 52]]

while True:
    num = input("찾을 값: ")
    if num.isdigit():
        for n in range(2):
            for m in range(4):
                if(int(num) == data[n][m]):
                    print("위치: ",n,",",m)
                    m=0
                    break
            if(n == 0 and m == 0):
                break
        m+=1
        if(n == 1 and m == 4):
            print("찾지 못함")
            break
    else:
        print("숫자 아님")