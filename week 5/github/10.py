import re


def re(s):
    a = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', a).lower()

s = str(input())
print(re(s))