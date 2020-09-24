import numpy as np
import time
import matplotlib.pyplot as plt
def bubble_sort(R):
    for num in range(len(R) - 1, 0, -1):
        for item in range(num):
            if R[item] > R[item + 1]:
                R[item], R[item + 1] = R[item + 1], R[item]
    return R

M5=[]
n = 0
while n <=150:
    Z = np.random.random(n)
    k = 0.0
    for ii in range(5):
        start_time = time.time()
        bubble_sort(Z)
        k+=(time.time() - start_time)
    M5.append(k/5)
    n = n + 1
print(M5)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.plot(M5)
plt.show()