from math import sqrt

sum = 0
sum_sq = 0
x = int(input())
a = 0

while x != 0:
 a += 1
 sum += x
 sum_sq += x ** 2
 x = int(input())
 
print(sqrt((sum_sq - sum ** 2 / a) / (a - 1)))