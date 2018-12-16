N = int(input())
G = input()
C = input()
acertos = 0
for i in range(N):
    if(G[i]==C[i]):
        acertos+=1
print(acertos)

