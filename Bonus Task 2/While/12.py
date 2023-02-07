max = 0
max2 = 0
a = int(input())

while a != 0:
    if max < a:
     max2 = max
     max = a
    elif max2 < a:
     max2 = a
    a = int(input())

print(max2)