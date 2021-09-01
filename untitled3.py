import random
buy = int(input("숫자입력: "))

lotto_num = []
for n in range(buy):
    number = range(1,47)
    lotto_num.append(random.sample(number,6))
print(lotto_num)