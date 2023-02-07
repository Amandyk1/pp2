a = int(input())

if a == 0:
    print(0)
else:
    x, y = 0, 1
    b = 1
    while y <= a:
        if y == a:
            print(b)
            break
        x, y = y, x + y
        b += 1
    else:
     print(-1)