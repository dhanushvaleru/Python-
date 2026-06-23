def summation(n):
    count=0
    if(n==0):
        return 0
    else:
        n=n//10
        count+=1
        return count+summation(n//10)
print(summation(1234))
