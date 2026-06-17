n=int(input('Enter the value:'))
k=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(f"{i}",end=" ")
        k+=1
    print()