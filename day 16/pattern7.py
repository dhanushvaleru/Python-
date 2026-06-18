n=int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(chr(i+96),end=" ")
    print()    