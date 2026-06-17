n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

s = 0

if a % 2 == 0:
    s += a

if b % 2 == 0:
    s += b

if c % 2 == 0:
    s += c

print(s)