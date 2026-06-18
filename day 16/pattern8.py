n=int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(chr(j+96),end=" ")
    print()    