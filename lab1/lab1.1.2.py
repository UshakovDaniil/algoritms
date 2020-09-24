import numpy as np
import time
import matplotlib.pyplot as plt
def sum (z):
    s=0
    for i in z: s+=i
M2=[]
n = 0
while n <=2000:
    Z = np.random.random(n)
    k = 0.0
    for ii in range(5):
        start_time = time.time()
        sum(Z)
        k+=(time.time() - start_time)
    M2.append(k/5)
    n = n + 1
print(M2)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.legend()
plt.plot(M2)
plt.show()