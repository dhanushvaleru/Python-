n=int(input())
for i in range(1,n+1):
    k=1
    for j in range(n,0,-1):
          if(j<=i):
            print(chr(i+96),end=" ")
          else:
            print(" ",end=" ")    
            k+=1
    print()    