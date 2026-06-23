def x(n):
    if(n<=1):
        return 10
        return  x(n-1)*n
    print(x(5))