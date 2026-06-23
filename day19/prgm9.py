def reverse_table(n, i=10):
    if i == 0:  
        return
    print(f"{n} x {i} = {n * i}")
    reverse_table(n, i - 1)  
n = int(input("Enter a number: "))
reverse_table(n)