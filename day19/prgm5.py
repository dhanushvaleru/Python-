def summation(n):
    rem,sum=0,0
    if(n==0):
        return 0
    else:
        rem=n%10
        sum=sum+rem
        return sum+summation(n//10)
print(summation(1234))