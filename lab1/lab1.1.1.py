
import numpy as np
import time
import matplotlib.pyplot as plt
def add (x):
    return x*0
M1=[]
n = 0
while n <=2000:
    Z = np.random.random(n)
    k = 0.0
    for ii in range(5):
        start_time = time.time()
        for i in Z:  (add (i))
        k+=(time.time() - start_time)
    M1.append(k/5)
    n = n + 1
print(M1)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.legend()
plt.plot(M1)
plt.show()
