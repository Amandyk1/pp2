def builtin(s):
    low = 0
    up = 0

    for i in range(len(s)):
        if s[i].islower():
            low += 1
        elif s[i].isupper():
            up += 1

    print(f"Lowers:{low}")
    print(f"Uppers:{up}")