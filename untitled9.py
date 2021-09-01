dic = {}

while True:
    eword = input("영어단어 입력: ")
    if eword == '':
        break
    
    if dic.get(eword):
        continue
    
    kword = input("한글해석 입력: ")
    dic = dict(zip(eword, kword))
    
while True:
    for v in dic.values:
        print(v)
        sco = input("영어 입력: ")
    
    if sco != dic.keys:
        
        
    break

print(dic)