cnt = 0
sum = 0
a = int(input())
while a != 0:
    cnt += 1
    sum += a
    a = int(input())
    b = sum/cnt
print(b)