n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

s = a + b + c

if s % 2 == 0:
    print("Even")
else:
    print("Odd")