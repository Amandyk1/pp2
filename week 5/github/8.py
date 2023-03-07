import re

s = input("")

a = re.findall('[A-Z][^A-Z]*', s)

print(a)