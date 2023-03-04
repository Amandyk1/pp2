def num():
    for i in range(0, n + 1, 2):
        yield i
n = int(input())
a = []
for x in num():
    a.append(str(x))
print(",". join(a))