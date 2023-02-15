def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"
s = str(input())
print(palindrome(s))