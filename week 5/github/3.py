import re

s = str(input())

a = re.findall('[a-z]+_[a-z]+', s)

print(a)


if a:
    print("Yes")
else:
    print("No")