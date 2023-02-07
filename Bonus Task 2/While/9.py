max = 0
i = -1
a = -1
b= 0

while a != 0:
    a = int(input())

    if a > max:
        max = a
        i = b
    b += 1
print(i)