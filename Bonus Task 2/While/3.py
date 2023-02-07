n = int(input())
x = 1
while n >= 2**x:
 x += 1
print(x - 1, 2**(x - 1))