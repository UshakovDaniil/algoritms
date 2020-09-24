import numpy as np
import time
import matplotlib.pyplot as plt
def mul (z):
    s=1
    for i in z: s*=i
M3=[]
n = 0
while n <=2000:
    Z = np.random.random(n)
    k = 0.0
    for ii in range(5):
        start_time = time.time()
        mul(Z)
        k+=(time.time() - start_time)
    M3.append(k/5)
    n = n + 1
print(M3)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.legend()
plt.plot(M3)
plt.show()