dic = {}

while True:
    str = input("영어단어와 한글해석을 빈칸으로 구분해 입력 하세요:")
    if str == '':
        break
    
    str.strip()
    pos = str.find(' ') #빈칸의 위치 구하기
    key = str[:pos].strip()
    val = str[pos+1:].strip()
    dic[key] = val
    
print("-----------저장된 단어장은----------")
print(dic)