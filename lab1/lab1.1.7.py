import numpy as np
import time
import matplotlib.pyplot as plt
def binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = int((start + end)/ 2)
    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)
    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)
    else:
        return mid

def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array

def merge(left, right):

    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def timsort(the_array):
    runs, sorted_runs = [], []
    l = len(the_array)
    new_run = [the_array[0]]
    for i in range(1, l):
        if i == l-1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        if the_array[i] < the_array[i-1]:
            if not new_run:
                runs.append([the_array[i-1]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(the_array[i])
    for each in runs:
        sorted_runs.append(insertion_sort(each))
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

M7=[]
n = 1
while n <=150:
    Z = np.random.random(n)
    k = 0.0
    for ii in range(5):
        start_time = time.time()
        timsort(Z)
        k+=(time.time() - start_time)
    M7.append(k/5)
    n = n + 1
print(M7)
plt.xlabel("Размерность")
plt.ylabel("Время")
plt.plot(M7)
plt.show()