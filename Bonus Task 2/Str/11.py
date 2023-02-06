a = str(input())

b = a[:a.find('h') + 1] 
c = a[a.find('h') + 1:a.rfind('h')]
d = a[a.rfind('h'):]
a = b + c.replace('h', 'H') + d

print(a)