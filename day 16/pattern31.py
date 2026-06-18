n=int(input())
k=1
for i in range(n,0,-1):
  for j in range(1,n+1):
    if(i<=j):
      print(chr(96+k),end=" ")
      k+=1
    else:
      print("",end=" ")
  print()