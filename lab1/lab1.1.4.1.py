import numpy as np
import time
import matplotlib.pyplot as plt
def p1 (z,x):
    k=0
    s = np.longlong(0.0)

    for i in z:
        s+=i*pow(x,k)
        k+=1
M4=[]
n = 0
while n <=1600:
    Z = np.random.random(n)
    k = 0.0
    for ii in range(5):
        start_time = time.time()
        p1(Z,1.5)
        k+=(time.time() - start_time)
    M4.append(k/5)
    n = n + 1
print(M4)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.legend()
plt.plot(M4)
plt.show()