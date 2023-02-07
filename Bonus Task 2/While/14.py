a = int(input())

if a == 0:
    print(0)
else:
    x, y = 0, 1
    for i in range(2, a + 1):
        x, y = y, x + y
    print(y)