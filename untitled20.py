dic = {}
cnn = 0
while True:
    a, b = input("영어단어와 한글해석을 빈칸으로 구분해 입력 하세요:").split()
    dic[a] = b
    cnn += 1
    
    if cnn == 4:
        break
    
print("-----------저장된 단어장은----------")
print(dic)