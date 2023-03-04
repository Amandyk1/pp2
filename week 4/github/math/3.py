import math

n = int(input())
l = int(input())
p = n * l
deg = 180 / n
tang = int(math.tan(deg))
apophem = l / 2 / tang
S = apophem * p / 2
print(S)