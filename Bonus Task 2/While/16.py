x = -1
curr_r = 0
max_r = 0
a = int(input())
while a != 0:
    if x == a:
        curr_r += 1
    else:
        x = a
        max_r = max(max_r, curr_r)
        curr_r = 1
    a = int(input())
max_r = max(max_r, curr_r)
print(max_r)