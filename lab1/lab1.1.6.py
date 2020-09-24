import numpy as np
import time
import matplotlib.pyplot as plt
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
M6=[]
n = 0
while n <=150:
    Z = np.random.random(n)
    k = 0.0
    for ii in range(5):
        start_time = time.time()
        quickSort(Z,0,len(Z)-1)
        k+=(time.time() - start_time)
    M6.append(k/5)
    n = n + 1
print(M6)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.plot(M6)
plt.show()