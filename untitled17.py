h2b = { '0000':'0', '0001':'1', '0010':'2', '0011':'3',
       '0100':'4', '0101':'5', '0110':'6', '0111':'7',
       '1000':'8', '1001':'9', '1010':'a', '1011':'b',
       '1100':'c', '1101':'d', '1110':'e', '1111':'f' };

def bin2hex(bin):
    if h2b[bin]:
        hex = h2b[bin[-4:]]
        return (True, hex)
    else:
        return (False, hex)
    
while True:
    bin = input("2진수 입력 : ")
    (confirm, hex) = bin2hex(bin)
    if confirm:
        print(" =>", bin, ":", hex)
    else:
        print(" => 2진수가 아니어서 종료합니다")
        break