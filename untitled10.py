dic = {}
miss = {}

while True:
    eng = input("영어단어 입력: ")
    
    if eng == '':
        print("단어 입력을 종료하고 영어단어 시험단계로 진입")
        break
    
    if eng in dic.keys():
        print("이미 등록되어 있는 단어")
        continue
    else:
        kor = input("한글 해석: ")
        dic[eng] = kor
    
print("------영어시험단계-------")

for k, v in dic.items():
    test = input(v+"?")
    
    if test != k:
        miss[k] = v
        
print("------틀린 문제-----")
print(miss)

    
    