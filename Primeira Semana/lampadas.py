N = int(input())
L = input().split()

A=False
B=False
for i in range(N):
    I = int(L[i])
    A = not A
    if (I == 2):
        B = not B

print(int(A))
print(int(B))
