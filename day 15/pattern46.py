n=int(input('Enter the value:'))
for i in range(1,n+1):
    flag=n-i
    stars=(2*i)-1
    print(" "*flag+f"{i}"*stars)