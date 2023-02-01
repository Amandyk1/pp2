n = int(input())
m = int(input())
a = int(input())
b = int(input())

if n > m:
    n, m = m, n
if a >= n / 2:
    a = n - a
if b >= m / 2:
    b = m - b

if a < b:
    print(a)
else:
    print(b)