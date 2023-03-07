import re
def re(s):
    return ''.join(x.capitalize() or '_' for x in s.split('_'))


a = str(input(""))

print(re(a))