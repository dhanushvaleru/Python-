n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

new_num = c * 100 + b * 10 + a

print(new_num)