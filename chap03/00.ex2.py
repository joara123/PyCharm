import numpy as np

#np.random.seed(10)
a = np.random.randint(0, 51, 500)
b = np.zeros((1, 51))

for i in a:
    for j in range(51):
        if (i == j):
            b[0][j] += 1

big1, big2, big3 = b[0][0], b[0][1], b[0][2]
cnt1, cnt2, cnt3 = 0, 0, 0

count = 0
for ii in b[0]:
    if(big1 < ii):
        big1 = ii
        cnt1 =count
    elif(big2 < ii):
        if(big2 == big1):
            break
        big2 = ii
        cnt2 =count
    elif(big3 < ii):
        if(big3 == big1):
            if(big3 == big2):
                break
        big3 = ii
        cnt3 = count
    count = count + 1

#print(a)
#print(b)
print(big1)
print(big2)
print(big3)
print(cnt1)
print(cnt2)
print(cnt3)
