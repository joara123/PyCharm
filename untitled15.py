data = []
peak_index = []

while True:
    val = int(input("숫자(0 종료): "))
    
    if val == 0:
        break
    data.append(val)
    
print("data= ",data)

for i in range(-1,len(data)-1):
    if(data[i-1] < data[i]) and (data[i] > data[i+1]):
        if(i >= 0):
            peak_index.append(i)
        else:
            peak_index.append(i+len(data))

print("peak_index= ",sorted(peak_index))