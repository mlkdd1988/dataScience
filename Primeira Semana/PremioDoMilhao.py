N = int(input())
milhao = 1000000
soma = 0
for i in range(N):
    soma+= int(input())
    if(soma>=milhao):
        print(i+1)
        break