a = int(input())
b = a // 60
c = a % 60
while b > 23:
    b = b - 24

print(b, c)