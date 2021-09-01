alist = [2, 1, -3, 1, -4, 1, 1, 3, -5, 4]

alist = [0] + alist
summ = [0]*len(alist)

for i in range(1, len(alist)):
    summ[i] = summ[i-1] + alist[i]
    
summ = summ[1:]
print(alist)
maxx = summ[0]

for i in range(0,len(alist)-1):
    for j in range(0,i):
        print(i,j,alist[j]-alist[i-1])
        maxx = max(maxx, alist[j]-alist[i-1])
        
print("max",maxx)
