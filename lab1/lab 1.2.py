import numpy as np
import time
import matplotlib.pyplot as plt
M8=[]
n = 1
while n <=150:
    Z = np.random.random(n)
    k = 0.0

    for ii in range(5):
        a = np.random.randint(214748367, size=(n, n), dtype=np.uint64)
        b = np.random.randint(214748367, size=(n, n), dtype=np.uint64)
        start_time = time.time()
        np.dot(a,b)
        k+=(time.time() - start_time)
    M8.append(k/5)
    n = n + 1
print(M8)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.legend()
plt.plot(M8)
plt.show()