def n33(n):
    return any(n[i + 1] == n[i] == 3 for i in range(len(n) - 1))

n = list(map(int, input().split()))
print(n33(n))