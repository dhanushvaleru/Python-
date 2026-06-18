n=int(input())
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(k+96),end=" ")
        k+=1
    print()    