data = []
peak_index=[] 

while True:
    num = int(input("숫자입력: "))
    if num == 0:
        break;
    else:
        data.append(num)
        
#처음
if data[0]>data[1]:
    peak_index.append(0)

#중간
count = 0
while True:
    if data[count]<data[count+1]:
        peak_index.append(count+1)
    count+=1
    
    if count == len(data)-2:
        break

#끝
if data[len(data)-1]>data[0]:
    peak_index.append(len(data)-1)
    
print('data=',data)
print('peak_index=',peak_index)