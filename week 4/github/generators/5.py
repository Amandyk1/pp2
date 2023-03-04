def gen():
    for x in range(n, -1, -1):
        yield x

n = int(input())
for y in gen():
    print(y)