n=int(input('Enter the value:'))
k=1
for i in range(1,n+1):
    for j in range(n+1):
        print("{:2d}".format(k),end=" ")
        k+=2
    print()