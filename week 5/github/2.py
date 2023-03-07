import re

s = input()
a = re.search('ab{2,3}', s)

print(a)

if a:
    print("Yes")
else:
    print("No")