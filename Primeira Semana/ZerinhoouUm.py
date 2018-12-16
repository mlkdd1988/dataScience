A,B,C = input().split()
if (A==B==C):
    print("*")
elif (A==B!=C):
    print("C")
elif (A==C!=B):
    print("B")
else:
    print("A")
