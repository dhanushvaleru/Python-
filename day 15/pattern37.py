n=int(input('Enter the value:'))
for i in range(1,n+1):
    k=1
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(f"{i*i}",end=" ")  
        k+=1 
    print()