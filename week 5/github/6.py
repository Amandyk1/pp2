import re

s = str(input())
a = re.sub('[ ,.]', ":", s)

print(a)