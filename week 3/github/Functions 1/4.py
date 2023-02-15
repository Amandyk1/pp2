def filter_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())

list = list()
for i in range(n):
    a = int(input())
    if filter_prime(a):
        list.append(a)
print(list)