def squares():
    for x in range(a, b + 1):
        yield x * x
a = int(input())
b = int(input())
for y in squares():
    print(y)