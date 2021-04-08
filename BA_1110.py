n = num = int(input())
count = 0
while True:
    a = n // 10
    b = n % 10
    total = a + b
    count += 1
    n = int(str(n % 10) + str(total % 10))
    if(num == n):
        break
print(count)
