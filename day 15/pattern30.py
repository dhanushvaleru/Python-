n = int(input())
k=1
for i in range(1, n + 1):
    for j in range(n - i + 1):
        print(f"{i*i}", end=" ")
        k+=2
    print()