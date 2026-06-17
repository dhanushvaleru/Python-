n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)