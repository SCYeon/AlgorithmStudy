import sys

D, K = map(int, input().split())

a = 0
a_current = 1
b = 1
b_current = 1

day = 3

while day != D:
    a, a_current = a_current, a
    a_current += a

    b, b_current = b_current, b
    b_current += b

    day+=1

A = 1
state = False
while True:
    B = 1
    while True:
        check=a_current * A + b_current * B
        if check > K:
            break
        elif check == K:
            state = True
            break
        B+= 1
    if state:
        break
    A+=1
print(A)
print(B)
