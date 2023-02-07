max = 0
a = int(input())
cnt = 1
while a != 0:
    if max < a:
     max = a
     cnt = 1
    elif a == max:
       cnt += 1 
     
    a = int(input())
print(cnt)