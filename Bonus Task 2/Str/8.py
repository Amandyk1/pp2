x = str(input())

a = x[:x.find('h')] 
b = x[x.find('h'):x.rfind('h') + 1]
c = x[x.rfind('h') + 1:]

x = a + b[::-1] + c
print(x)