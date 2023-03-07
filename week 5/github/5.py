import re

s = str(input())
a = re.search('a.*b$', s)

print(a)

if a:
    print("Yes")
else:
    print("No")