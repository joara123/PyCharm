import numpy as np

data = [0.5, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
arr = np.array(data)

hap = np.sum(data)
avg = np.mean(data)

print('합: ', round(hap, 2))
print('평균: ', round(avg, 2))

