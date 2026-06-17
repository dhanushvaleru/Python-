n = int(input())
k=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(f"{j*j}", end=" ")
        k+=2
    print()