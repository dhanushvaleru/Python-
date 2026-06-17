n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

print(a**2 + b**2 + c**2)