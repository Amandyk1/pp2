import re

s = str(input())
a = re.search('[A-Z]+[a-z]+$', s)

print(a)

if a:
    print("Yes")
else:
    print("No")