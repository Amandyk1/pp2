a = int(input())
sum = 0
for x in range(1, a + 1):
    sum += x
for x in range(a - 1):
    sum -= int(input())
print(sum)
