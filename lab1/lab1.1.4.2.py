import numpy as np
import time
import sys
import matplotlib.pyplot as plt
sys.setrecursionlimit(5000)
def p2 (z,x,i,max):
    if i+1<max:
        return p2(z,x,i+1,max)*x+z[i]
    else:return z[max]*x+z[i]
M41=[]
n = 1
while n <=1600:
    Z = np.random.random(n)
    k = 0.0
    for ii in range(5):
        start_time = time.time()
        p2(Z,1.5,0,n-1)
        k+=(time.time() - start_time)
    M41.append(k/5)
    n = n + 1
print(M41)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.legend()
plt.plot(M41)
plt.show()