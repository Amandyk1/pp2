from datetime import datetime, timedelta
a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
x = datetime(a1, b1, c1)
y = datetime(a2, b2, c2)
d = x - y
print((x - y).total_seconds())