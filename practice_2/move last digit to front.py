n = int(input())

a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

new_num = d * 1000 + a * 100 + b * 10 + c

print(new_num)