import math
N = int(input())
L = input().split()

for i in range(len(L)):
    x = float(L[i])
    print("{0:.4f}".format(math.sqrt(x)))
