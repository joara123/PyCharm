print('입력 받은 수 까지의 n의 배수를 만듭니다.')
n = int(input('n? '))
num = int(input('어디까지 할까요? '))

lst =[]
for i in range(1,num+1):
    if i%n == 0:
        lst.append(i)
print(lst)

num1 = int(input('위 리스트이 모든 원소에 더할 값? '))
x = list(map(lambda x:x+num1,lst))
print(x)