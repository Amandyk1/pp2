def builtin(s):
    reverse = "".join(reversed(s))
    print(reverse)

    if s == reverse:
        print("Palindrome")
    else:
        print("Not palindrome")