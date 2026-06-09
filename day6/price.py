Price=list(map(int,input('Enter the prices:').split()))
print([i for i in Price if i>1000])