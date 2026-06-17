n=int(input('Enter the value:'))
k=1
for i in range(1,n+1):
    for j in range(1,n):
        print(f"{j*j}",end=" ")
        k+=1
    print()