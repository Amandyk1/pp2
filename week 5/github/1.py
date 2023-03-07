import re
s = str(input())
a = re.search('ab*', s)

print(a)

if a:
    print("Yes")
else:
    print("No")