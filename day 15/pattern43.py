5.
n=int(input('Enter the integer :'))
for i in range(1,n+1):
    for j in range(n,0,-1):
      if(j<=i):
        if(i%2==0):
          print(0,end=" ")
        else:
          print(1,end=" ")
      else:
        print(f"",end=" ")
    print()