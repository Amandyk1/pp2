a = input()
b = a[:a.find('h')] + a[a.rfind('h') + 1:]
print(b)
