import numpy as np
import random

M = int(input("введіть кількість рядків M: "))
N = int(input("введіть кількість стовпців N: "))

A = np.zeros((M, N), dtype=int)

for i in range(M):
    for j in range(N):
        A[i][j] = random.randint(0,1)

print("\nпочатковий масив A: ")
print(A)

res = np.zeros((M, N + 1), dtype=int)

for i in range(M):
    count_ones = 0 
    for j in range(N):
        res[i][j] = A[i][j]
        if A[i][j] == 1:
            count_ones = count_ones + 1

    if count_ones % 2 != 0:
        res[i][N] = 1
    else:
        res[i][N] = 0

print("\nмасив А з доданим стовпчиком ( кількість одиниць у кожному рядку парну ):")
print(res)

