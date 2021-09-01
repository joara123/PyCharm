import numpy as np

a = np.array([0,10,20,30,40,50])
b = np.array([0,20])

print("a배열: ", a)
print("b배열: ", b)

t = np.full(a.shape, False)
print(t)

index = 0
for x in a:
    if x in b:
        t[index] = True
    index += 1
        
print("t배열: ",t)