a = int(input())
b = int(input())
c = int(input())
d = int(input())

n = abs(a - c)
m = abs(b - d)

if n == 1 and m == 2 or n == 2 and m == 1:
    print("YES")
else:
    print("NO")