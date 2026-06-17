n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

sum_cubes = a**3 + b**3 + c**3

if sum_cubes == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")