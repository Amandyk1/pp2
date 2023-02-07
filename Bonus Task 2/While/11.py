a = int(input())
cnt = 0
while a != 0:
    b = int(input())
    if b != 0 and a < b:
        cnt += 1
    a = b
print(cnt)