a = int(input())
b = int(input())
c = int(input())

d = a + b + c

if d % 2 == 1:
    d = (d + 1) // 2
else:
    d = d // 2
print(d)
