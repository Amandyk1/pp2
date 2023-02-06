a = str(input())
b = ''

for x in range(len(a)):
    if x % 3 != 0:
        b = b + a[x]
print(b)