n = int(input())

temp = n
sum_fact = 0

while n > 0:
    d = n % 10

    fact = 1
    for i in range(1, d + 1):
        fact *= i

    sum_fact += fact
    n //= 10

if sum_fact == temp:
    print("Strong Number")
else:
    print("Not Strong Number")