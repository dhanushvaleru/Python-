n=int(input())
for i in range(n,0,-1):
    k=1
    for j in range(n,0,-1):
          if(j<=i):
            print(chr(k+96),end=" ")
          else:
            print(" ",end=" ")    
            k+=1
    print()    