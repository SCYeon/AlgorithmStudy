def f(x, y, w):
    h1 = (x**2-w**2)**0.5
    h2 = (y**2-w**2)**0.5    
    c = h1*h2 / (h1+h2)
    return c
    
x, y, c = map(float, input().split())
a, b = 0, min(x, y)
res = 0
while b-a > 0.000001:
    m = (a+b)/2
    if f(x, y, m) >= c:
        res = m
        a = m
    else:
        b = m
print(res)
