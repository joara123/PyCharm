import numpy as np
import random
ran_num = []
for n in random.sample(range(1,101),10):
    ran_num.append(n)
print("ran_num = ",ran_num)
ran_numb = np.array(ran_num)
mul = ran_numb[ran_numb % 5 == 0]
print(mul)