n=int(input())
for i in range(n,0,-1):
    k=0
    for j in range(n,0,-1):
        if(j<=i):
            k+=1
            print(chr(k+96),end=" ")
        else:
            print(f" ",end=" ")
    print()    