def print_n_to_1(n):
    if n==0:
        return
    print_n_to_1(n-1)
    print(n,end=" ")
print_n_to_1(5)
